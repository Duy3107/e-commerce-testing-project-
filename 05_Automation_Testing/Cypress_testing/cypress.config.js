const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    reporter: 'mochawesome',
    reporterOptions: {
      reportDir: 'cypress/report/mochawesome-report',
      overwrite: false,
      html: false,
      json: true,
    },

    setupNodeEvents(on, config) {
      // implement node event listeners here nếu cần
      return config;
    },
  },
});
