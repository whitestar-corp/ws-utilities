import {Client, ApiResponse, RequestParams } from '@elastic/elasticsearch'
import { eventNames } from 'node:process';
import { toASCII } from 'node:punycode';
import { brotliCompress } from 'node:zlib';
import request  from "request-promise-native";

var estester: WESTester;
//const client:Client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});
class WESTester
{

    watchBox: HTMLInputElement;

    constructor()
    {

        this.watchBox = document.getElementById("search_box2") as HTMLInputElement;
        this.watchBox.onkeyup = this.handleTextChange;

        var testb = document.getElementById("testButton");
        testb.onmousedown = this.pingTest;
//        this.client = new Client({ node: 'https://quorum:1aCa4319$@es.whitestar.com'});
//        this.client.ping();
    } 

    handleTextChange():void{
        if(!this.watchBox)
            this.watchBox = document.getElementById("search_box2") as HTMLInputElement;
        console.log(this.watchBox.value);
        //console.log(client);
    }
    async pingTest(){
        try {
            console.log('ping test');
            //var client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});
            //var pingresult = client.ping();
            //console.log(pingresult);
            var header = new Headers();
            var username = 'quorum';
            var password = '1aCa4319$';

            header.append('Authorization', 'Basic ' + btoa(username + ':' + password));          
            const response = await fetch('https://es.whitestar.com',{headers: header});

            const data = await response.json();
            if(response.ok)
            {
                console.log(data);
                console.log(data?.name);
                console.log(data?.tagline);

                document.getElementById("viewDiv").innerHTML = JSON.stringify(data);
                var showme:string;
                Object.keys(data).forEach(function(key) {
                    showme += 'Key : ' + key + ', Value : ' + data[key] + "<br>";
                  })

                document.getElementById("viewDiv").innerHTML += showme;


            }

        } catch (error) {
            console.log(error);
        }
        //var client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});
        //client.ping();

    }
}

estester = new WESTester();

function onTextModified(tb:Text)
{
    alert("yo");
}