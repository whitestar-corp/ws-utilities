import {Client, ApiResponse, RequestParams } from '@elastic/elasticsearch'
import { eventNames } from 'node:process';
import { brotliCompress } from 'node:zlib';

var dork: Dorky;
//const client:Client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});

console.log("yo");

class Dorky
{

    watchBox;

    constructor()
    {

        this.watchBox = document.getElementById("search_box2");
        this.watchBox.onkeyup = this.handleTextChange;

        var testb = document.getElementById("testButton");
        testb.click = this.pingTest;
//        this.client = new Client({ node: 'https://quorum:1aCa4319$@es.whitestar.com'});
//        this.client.ping();
    } 

    handleTextChange():void{
        var tb = document.getElementById("search_box2") as HTMLInputElement;
        console.log(tb.value);
        //console.log(client);
    }
    pingTest():void{
        try {
            //var client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});
            //client.ping();
        } catch (error) {
            console.log(error);
        }
        //var client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});
        //client.ping();
    }
}

dork = new Dorky();

function onTextModified(tb:Text)
{
    alert("yo");
}