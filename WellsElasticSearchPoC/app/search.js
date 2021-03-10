"use strict";
exports.__esModule = true;
var elasticsearch_1 = require("@elastic/elasticsearch");
var client = new elasticsearch_1.Client({ node: '' });
console.log("yo");
function onTextModified(e) {
    console.log(e.value);
}
