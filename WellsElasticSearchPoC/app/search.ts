import {Client, ApiResponse, RequestParams } from '@elastic/elasticsearch'

const client = new Client({ node: ''});


console.log("yo");

function onTextModified(e)
{
    console.log(e.value);
}