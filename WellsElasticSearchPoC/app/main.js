var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
define(["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var estester;
    var ws_es_url = 'https://es.whitestar.com';
    var user_name = 'quorum';
    var password = '1aCa4319$';
    //const client:Client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});
    var WESTester = /** @class */ (function () {
        function WESTester() {
            this.watchBox = document.getElementById("search_box2");
            this.watchBox.onkeyup = this.fetchTest;
            var testb = document.getElementById("testButton");
            testb.onmousedown = this.pingTest;
            var testclient = document.getElementById("testClient");
            testclient.onmousedown = this.clientTest;
            document.getElementById('testFetch').onmouseup = this.fetchTest;
            //        this.client = new Client({ node: 'https://quorum:1aCa4319$@es.whitestar.com'});
            //        this.client.ping();
        }
        WESTester.prototype.handleTextChange = function () {
            if (!this.watchBox)
                this.watchBox = document.getElementById("search_box2");
            console.log(this.watchBox.value);
            //console.log(client);
        };
        WESTester.prototype.pingTest = function () {
            return __awaiter(this, void 0, void 0, function () {
                var header, username, password, response, data_1, showme, error_1;
                return __generator(this, function (_a) {
                    switch (_a.label) {
                        case 0:
                            _a.trys.push([0, 3, , 4]);
                            console.log('ping test');
                            header = new Headers();
                            username = 'quorum';
                            password = '1aCa4319$';
                            header.append('Authorization', 'Basic ' + btoa(username + ':' + password));
                            return [4 /*yield*/, fetch('https://es.whitestar.com', { headers: header })];
                        case 1:
                            response = _a.sent();
                            return [4 /*yield*/, response.json()];
                        case 2:
                            data_1 = _a.sent();
                            if (response.ok) {
                                console.log(data_1);
                                console.log(data_1 === null || data_1 === void 0 ? void 0 : data_1.name);
                                console.log(data_1 === null || data_1 === void 0 ? void 0 : data_1.tagline);
                                document.getElementById("viewDiv").innerHTML = JSON.stringify(data_1);
                                Object.keys(data_1).forEach(function (key) {
                                    showme += 'Key : ' + key + ', Value : ' + data_1[key] + "<br>";
                                });
                                document.getElementById("viewDiv").innerHTML += showme;
                            }
                            return [3 /*break*/, 4];
                        case 3:
                            error_1 = _a.sent();
                            console.log(error_1);
                            return [3 /*break*/, 4];
                        case 4: return [2 /*return*/];
                    }
                });
            });
        };
        WESTester.prototype.fetchTest = function () {
            return __awaiter(this, void 0, void 0, function () {
                var headers, esindex, middlebits, searchprefix, searchfield, u, response, data, showtable, i;
                return __generator(this, function (_a) {
                    switch (_a.label) {
                        case 0:
                            headers = new Headers();
                            headers.append('Authorization', 'Basic ' + btoa(user_name + ':' + password));
                            esindex = document.getElementById("esindex").value;
                            middlebits = '/' + esindex + '/_search';
                            searchprefix = document.getElementById("search_box2").value;
                            //  https://es.whitestar.com/us_header/_search?q=%22KER*%22&from=0&size=20
                            if (searchprefix.length < 1)
                                return [2 /*return*/];
                            searchfield = document.getElementById("seachfield").value;
                            if (searchfield != "_all")
                                searchprefix = searchfield + ":" + searchprefix;
                            u = ws_es_url + middlebits + '?' + "q=" + searchprefix + '*&' + 'size=20&from=0';
                            return [4 /*yield*/, fetch(u, { headers: headers })];
                        case 1:
                            response = _a.sent();
                            return [4 /*yield*/, response.json()];
                        case 2:
                            data = _a.sent();
                            if (response.ok) {
                                console.log(data);
                                document.getElementById("viewDiv").innerHTML = '<br>Hits: ' + data.hits.total + '<br>';
                                showtable = "<table><tr>";
                                Object.keys(data.hits.hits[0]["_source"]).forEach(function (key) {
                                    showtable += "<td>" + key + "</td>";
                                });
                                showtable += "</tr>";
                                for (i = 0; i < data.hits.hits.length; i++) {
                                    showtable += "<tr>";
                                    Object.keys(data.hits.hits[i]["_source"]).forEach(function (key) {
                                        showtable += "<td>" + data.hits.hits[i]["_source"][key] + "</td>";
                                    });
                                    showtable += "/<tr>";
                                }
                                showtable += "</tr></table>";
                                document.getElementById("viewDiv").innerHTML += showtable;
                            }
                            return [2 /*return*/];
                    }
                });
            });
        };
        WESTester.prototype.clientTest = function () {
            return __awaiter(this, void 0, void 0, function () {
                return __generator(this, function (_a) {
                    return [2 /*return*/];
                });
            });
        };
        return WESTester;
    }());
    estester = new WESTester();
    function onTextModified(tb) {
        alert("yo");
    }
});
