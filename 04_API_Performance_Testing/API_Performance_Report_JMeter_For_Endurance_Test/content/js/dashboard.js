/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 99.49308755760369, "KoPercent": 0.5069124423963134};
    var dataset = [
        {
            "label" : "FAIL",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "PASS",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.6440092165898618, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [0.6672025723472669, 500, 1500, "API_TC_007 Create Account"], "isController": false}, {"data": [0.6451612903225806, 500, 1500, "API_TC_003 Search Product"], "isController": false}, {"data": [0.6993569131832797, 500, 1500, "API_TC_002 Get all brands"], "isController": false}, {"data": [0.6919354838709677, 500, 1500, "API_TC_005 Verify login valid"], "isController": false}, {"data": [0.6375404530744336, 500, 1500, "API_TC_010 Delete an existing Account"], "isController": false}, {"data": [0.5016025641025641, 500, 1500, "API_TC_001 Get all products"], "isController": false}, {"data": [0.6661237785016286, 500, 1500, "API_TC_012 Error Handling invalid endpoint"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 2170, 11, 0.5069124423963134, 1423.838248847926, 301, 125176, 587.0, 1131.6000000000004, 1904.3499999999995, 15931.509999999744, 1.2698709939812796, 3.590716134822847, 0.31638593965333106], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["API_TC_007 Create Account", 311, 1, 0.3215434083601286, 1318.8231511254023, 335, 125169, 573.0, 927.2000000000014, 1701.1999999999998, 8333.679999999982, 0.18318459647260685, 0.16384248797372508, 0.08306131592657537], "isController": false}, {"data": ["API_TC_003 Search Product", 310, 2, 0.6451612903225806, 1641.5032258064512, 315, 90293, 587.0, 1558.0000000000018, 2082.0499999999993, 61792.2399999995, 0.1830884181219735, 0.33274866544784903, 0.044699320830559934], "isController": false}, {"data": ["API_TC_002 Get all brands", 311, 0, 0.0, 1021.7234726688107, 301, 45978, 521.0, 1049.0000000000005, 2157.799999999998, 8266.239999999998, 0.18314306476668987, 0.3590993238649547, 0.0252179415352571], "isController": false}, {"data": ["API_TC_005 Verify login valid", 310, 2, 0.6451612903225806, 1381.841935483871, 360, 125068, 537.5, 1065.7000000000028, 1705.5499999999995, 19139.26999999978, 0.18309944839814563, 0.16679561457625178, 0.049153757540301074], "isController": false}, {"data": ["API_TC_010 Delete an existing Account", 309, 3, 0.970873786407767, 838.2135922330094, 398, 23822, 608.0, 1044.0, 1709.0, 5259.999999999983, 0.1827957816176066, 0.16701917739975664, 0.05742640029554942], "isController": false}, {"data": ["API_TC_001 Get all products", 312, 2, 0.6410256410256411, 2101.118589743589, 371, 125176, 607.0, 1358.099999999999, 2255.499999999998, 72138.98000000001, 0.18272681111845793, 1.1418343846469652, 0.025517513662050274], "isController": false}, {"data": ["API_TC_012 Error Handling invalid endpoint", 307, 1, 0.3257328990228013, 1661.3192182410428, 311, 103110, 626.0, 1192.5999999999995, 2174.799999999999, 62498.360000000575, 0.18242666685681824, 1.289590709134644, 0.03402684899380106], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["Test failed: text expected to contain /{&quot;responseCode&quot;: 200, &quot;message&quot;: &quot;User exists!&quot;}/", 1, 9.090909090909092, 0.04608294930875576], "isController": false}, {"data": ["Non HTTP response code: java.net.SocketException/Non HTTP response message: Socket closed", 2, 18.181818181818183, 0.09216589861751152], "isController": false}, {"data": ["520/&lt;none&gt;", 4, 36.36363636363637, 0.18433179723502305], "isController": false}, {"data": ["524/&lt;none&gt;", 3, 27.272727272727273, 0.1382488479262673], "isController": false}, {"data": ["Test failed: text expected to contain /{&quot;responseCode&quot;: 200, &quot;message&quot;: &quot;Account deleted!&quot;}/", 1, 9.090909090909092, 0.04608294930875576], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 2170, 11, "520/&lt;none&gt;", 4, "524/&lt;none&gt;", 3, "Non HTTP response code: java.net.SocketException/Non HTTP response message: Socket closed", 2, "Test failed: text expected to contain /{&quot;responseCode&quot;: 200, &quot;message&quot;: &quot;User exists!&quot;}/", 1, "Test failed: text expected to contain /{&quot;responseCode&quot;: 200, &quot;message&quot;: &quot;Account deleted!&quot;}/", 1], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": ["API_TC_007 Create Account", 311, 1, "524/&lt;none&gt;", 1, "", "", "", "", "", "", "", ""], "isController": false}, {"data": ["API_TC_003 Search Product", 310, 2, "520/&lt;none&gt;", 2, "", "", "", "", "", "", "", ""], "isController": false}, {"data": [], "isController": false}, {"data": ["API_TC_005 Verify login valid", 310, 2, "Test failed: text expected to contain /{&quot;responseCode&quot;: 200, &quot;message&quot;: &quot;User exists!&quot;}/", 1, "524/&lt;none&gt;", 1, "", "", "", "", "", ""], "isController": false}, {"data": ["API_TC_010 Delete an existing Account", 309, 3, "Non HTTP response code: java.net.SocketException/Non HTTP response message: Socket closed", 2, "Test failed: text expected to contain /{&quot;responseCode&quot;: 200, &quot;message&quot;: &quot;Account deleted!&quot;}/", 1, "", "", "", "", "", ""], "isController": false}, {"data": ["API_TC_001 Get all products", 312, 2, "520/&lt;none&gt;", 1, "524/&lt;none&gt;", 1, "", "", "", "", "", ""], "isController": false}, {"data": ["API_TC_012 Error Handling invalid endpoint", 307, 1, "520/&lt;none&gt;", 1, "", "", "", "", "", "", "", ""], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
