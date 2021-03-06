const path = require("path");
const merge = require("webpack-merge");
const webpack = require("webpack");

const common = require("./webpack.common.js");

const serverName = process.env.JS_SERVER || "agir.local";
const port = process.env.JS_SERVER
  ? +process.env.JS_SERVER.split(":")[1] || 3000
  : 3000;

module.exports = merge.merge(common, {
  mode: "development",
  output: {
    publicPath: `http://${serverName}:${port}/static/components/`,
    devtoolModuleFilenameTemplate: "webpack://[absolute-resource-path]",
    filename: "[name]-[hash].js",
  },
  watchOptions: {
    poll: 1000,
  },
  devServer: {
    publicPath: `http://${serverName}:${port}/static/components/`,
    public: `${serverName}:${port}`,
    contentBase: path.join(__dirname, "/assets/components/"),
    compress: true,
    hot: true,
    hotOnly: true,
    host: serverName === "localhost" ? "localhost" : "0.0.0.0",
    port: port,
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    allowedHosts: ["agir.local"], // l'appli Django est toujours sur agir.local
  },
  optimization: {
    namedModules: true,
    noEmitOnErrors: true,
  },
  plugins: [new webpack.HotModuleReplacementPlugin()],
  resolve: {
    alias: {
      "react-dom": "@hot-loader/react-dom",
    },
  },
});
