
import React, { useState, useEffect } from 'react';
import AWS from 'aws-sdk';
//code to connect to aws cloud and retrieve data from a table that is created in cloud.
const dynamodb = new AWS.DynamoDB.DocumentClient({
  region: 'ap-south-1',
  accessKeyId: 'your-accesskey-id',
  secretAccessKey: 'your-secrectkey-id'
});

function CloudConnect() {
    const [data, setData] = useState([]);
  
    useEffect(() => {
      const fetchData = async () => {
        const result = await dynamodb.scan({ TableName: 'parking' }).promise();
        setData(result.Items);
      };
      fetchData();
    }, []);
  
    return (
      <div className="product-list">
        <h3 className="product-list-specifications">Slot Information</h3>
        <ul >
            <li className="new-update">Slot No</li>
            <li className="new-update">Status</li>
        </ul>
        <ul>
        {
                data.length>0 ? data.map((item)=>
                <ul >
                    
                    <li className="new-update">{item.slot_no}</li>
                    <li className="new-update">{item.status}</li>
                </ul>
                )
                : <h1>No Slots Present</h1>
            }
        </ul>
      </div>
    );
  }
  
  export default CloudConnect;
  