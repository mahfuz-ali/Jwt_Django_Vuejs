// Weather.vue

<template>
  <div>
    <h1>My Weather App</h1>
  </div>
</template>

<script>
const SECRET_NUM = 'MahfuzSecretKey'
var jwt = require('jsonwebtoken')
var token = jwt.sign({ username: 'admin', password: 'admin' }, SECRET_NUM)
console.log(token)

export default {
  name: 'Weather',
  created () {
    fetch('http://127.0.0.1:8000/api/jwt-communication/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: token
        // 'Access-Control-Allow-Origin': true
        // 'Content-Type': 'application/x-www-form-urlencoded',
      }
    })
      .then((response) => {
        return response
      }).then((data) => {
      // eslint-disable-next-line no-console
        console.log(data)
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
