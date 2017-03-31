var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");
var srcPath = path.resolve("./src/assets/");
var cssPath = path.resolve("./src/assets/css/");
var scssPath = path.resolve("./src/assets/sass/");

var ExtractTextPlugin = require("extract-text-webpack-plugin");
var CommonsPlugin = new require("webpack/lib/optimize/CommonsChunkPlugin")

process.traceDeprecation = true;

module.exports = {
  context: __dirname,
  //root: srcPath,
  // entry: "./src/assets/js/index",
  entry: {
    'main': "./src/assets/js/main/index",
    'login': "./src/assets/sass/login",
  },

  output: {
      // path: path.join(__dirname, "js"),
      path: path.resolve("./src/assets/bundles/"),
      filename: "[name].js",
      chunkFilename: "[name]-[id].js"
      // allChunks: true
  },
  plugins: [
      new ExtractTextPlugin("[name].css"),
      new CommonsPlugin({
              minChunks: 4,
              name: "common",
      }),
  ],
  module: {
      rules: [
         {
             test: /bootstrap-sass[\/\\]assets[\/\\]javascripts[\/\\]/,
             use: 'imports-loader?jQuery=jquery'
         },
         {
             test: /\.jsx?$/,
             exclude: /(node_modules|bower_components)/,
             loader: 'babel-loader',
             options: {
                       presets: ['es2015']
                     }
         },
         {
             test:/\.css$/,
             use: ExtractTextPlugin.extract(
                     {
                        fallback: "style-loader",
                        use: ["css-loader", "autoprefixer"]
                     }
                  )
                       
         },
         {
             test:/\.scss$/,
             use: ExtractTextPlugin.extract(
                     {
                       fallback: "style-loader",
                       use: ["css-loader", "sass-loader"]
                     }
                  ),
         },

         {
             test: /\.txt$/,
             use: "raw-loader",
         },

         {
             test: /\.(png|jpg|jpeg|gif|svg|woff|woff2|ico)$/,
             use:  "url-loader?limit=10000",
         },
         {
             test: /\.(eot|ttf|wav|mp3)$/,
             use:  "file-loader",
         },

      ],
  },
  resolve: {
      modules: [
          "./node_modules",
          "./bower_components",
           srcPath,
           cssPath,
           scssPath,
      ],
      extensions: 
           [".js", ".jsx", ".css", ".sass", ".csss"]
  }
}
