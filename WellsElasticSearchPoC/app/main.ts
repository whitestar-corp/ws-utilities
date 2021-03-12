import {Client, ApiResponse, RequestParams } from '@elastic/elasticsearch'
import { eventNames } from 'node:process';
import { toASCII } from 'node:punycode';
import { brotliCompress } from 'node:zlib';
import request, { head }  from "request-promise-native";
import {URL, URLSearchParams} from 'url'
import {stringify} from 'querystring';

var estester: WESTester;

const ws_es_url:string = 'https://es.whitestar.com';
const user_name:string = 'quorum';
const password:string = '1aCa4319$';

//const client:Client = new Client({node:'https://quorum:1aCa4319$@es.whitestar.com'});
class WESTester
{


    watchBox: HTMLInputElement;

    constructor()
    {

        this.watchBox = document.getElementById("search_box2") as HTMLInputElement;
        this.watchBox.onkeyup = this.fetchTest;

        var testb = document.getElementById("testButton");
        testb.onmousedown = this.pingTest;

        var testclient = document.getElementById("testClient");
        testclient.onmousedown = this.clientTest;

        document.getElementById('testFetch').onmouseup = this.fetchTest;

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
    async fetchTest()
    {
        var headers = new Headers();
        headers.append('Authorization', 'Basic ' + btoa(user_name + ':' + password));          

        
        var middlebits = '/us_header/_search'

        //var params = {size:20, from:0};

        var searchprefix = (document.getElementById("search_box2") as HTMLInputElement).value;
        //  https://es.whitestar.com/us_header/_search?q=%22KER*%22&from=0&size=20
        if(searchprefix.length <1)
            return;

        var u = ws_es_url + middlebits+ '?' + "q=" + searchprefix + '*&'+ 'size=20&from=0';
        const response = await fetch(u,{headers: headers});
        const data = await response.json();
        if(response.ok)
        {
            console.log(data);

            var hits = data.hits;
            document.getElementById("viewDiv").innerHTML = '<br>Hits: ' + data.hits.total +'<br>';
            var showkeys:string;
            var showme:string;
            var first = true;

            var showtable = "<table><tr>";
            
            Object.keys(data.hits.hits[0]["_source"]).forEach(function(key)
            {
                showtable += "<td>" + key + "</td>";
            })
            showtable += "</tr>";

            for(var i=0; i< data.hits.hits.length; i++)
            {
                showtable += "<tr>"
                Object.keys(data.hits.hits[i]["_source"]).forEach(function(key)
                {


                    showme += data.hits.hits[i]["_source"][key] + " ";
                    showtable += "<td>" + data.hits.hits[i]["_source"][key] + "</td>"
                })

                showme += '<br>'

                showtable += "/<tr>"
            }
            
            showtable += "</tr></table>";

            document.getElementById("viewDiv").innerHTML += showtable;
        }

        // curl -X GET 'https://quorum:1aCa4319$@es.whitestar.com/us_header/_search?pretty'
    }

    async clientTest()
    {
        //var client = new Client();
        //tscconsole.log(client);


/*
        // https://www.elastic.co/guide/en/elasticsearch/client/javascript-api/current/client-connecting.html
        var client = new Client({
            node:'https://es.whitestar.com' ,
            ssl: { rejectUnauthorized: false },
            auth: 
                {
                    username: 'quorum',
                    password: '1aCa4319$'
                }
            
        });
        //var s = client.security.authenticate();
        console.log(client.indices);
        /*
        client.search({
            index: 'tx_header',
            body: {
              query: {
                match: { hello: 'world' }
              }
            }
          }, (err, result) => {
            if (err) console.log(err)
          })
          */
    }
}

estester = new WESTester();

function onTextModified(tb:Text)
{
    alert("yo");
}