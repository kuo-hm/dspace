const express = require("express");
const axios = require("axios");
const app = express();
const PORT = 3005;
const token =
  "Bearer eyJhbGciOiJIUzI1NiJ9.eyJlaWQiOiJkZDYwNDcxYi1hYzhkLTRjN2ItYjE0Yi0zNzZkZDUxYjRlY2MiLCJzZyI6W10sImF1dGhlbnRpY2F0aW9uTWV0aG9kIjoicGFzc3dvcmQiLCJleHAiOjE2ODEzODIwNzN9._sbg7VGvlNXi_QNMp8P5hv7zmLUv2rVMt2Erhzwger0";

const body = {
  id: 12,
  name: "TESTE 1",
  handle: "123456789/14",
  type: "item",
  link: "/RESTapi/items/12",
  expand: [
    "metadata",
    "parentCollection",
    "parentCollectionList",
    "parentCommunityList",
    "bitstreams",
    "all",
  ],
  lastModified: "2015-01-29 15:51:04.049",
  parentCollection: null,
  parentCollectionList: null,
  parentCommunityList: null,
  bitstreams: null,
  archived: "true",
  withdrawn: "false",
};
app.get("/", async (req, res) => {
  axios
    .get("https://sbn.inpt.ac.ma/server/api/core/collections", {})
    .then((response) => {
      const cookieValue = response.headers["set-cookie"][0]
        .split(";")[0]
        .substring("DSPACE-XSRF-COOKIE=".length);
      axios
        .patch(
          `https://sbn.inpt.ac.ma/server/api/core/items/11/metadata`,
          body,
          {
            headers: {
              Cookie: `DSPACE-XSRF-COOKIE=${cookieValue}`,
              "X-XSRF-TOKEN": cookieValue,
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "*",
              "content-type": "multipart/form-data",
              authorization: token,
            },
          }
        )
        .then((responsee) => {
          console.log(responsee.headers);
          console.log("res", cookieValue);
          res.send(responsee.data);
        })
        .catch((error) => {
          console.log("err", cookieValue);
          res.send(error);
        });
    })
    .catch((error) => {
      console.log("catch", cookieValue);
      res.send(error);
    });
});
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
