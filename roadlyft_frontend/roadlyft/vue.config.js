const { defineConfig } = require('@vue/cli-service');
const webpack = require('webpack'); // Make sure webpack is imported

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port: 5500
  },
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
        '__VUE_PROD_HYDRATION_MISMATCH_DETAILS__': JSON.stringify(true)
      })
    ]
  }
});
