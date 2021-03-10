define(["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var dork;
    //const client:Client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});
    console.log("yo");
    var Dorky = /** @class */ (function () {
        function Dorky() {
            this.watchBox = document.getElementById("search_box2");
            this.watchBox.onkeyup = this.handleTextChange;
            var testb = document.getElementById("testButton");
            testb.click = this.pingTest;
            //        this.client = new Client({ node: 'https://quorum:1aCa4319$@es.whitestar.com'});
            //        this.client.ping();
        }
        Dorky.prototype.handleTextChange = function () {
            var tb = document.getElementById("search_box2");
            console.log(tb.value);
            //console.log(client);
        };
        Dorky.prototype.pingTest = function () {
            try {
                //var client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});
                //client.ping();
            }
            catch (error) {
                console.log(error);
            }
            //var client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});
            //client.ping();
        };
        return Dorky;
    }());
    dork = new Dorky();
    function onTextModified(tb) {
        alert("yo");
    }
});
