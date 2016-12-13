// Create a function called ready
//  - Embed this API endpoint as a <script> tag: https://api.github.com/orgs/greenfox-academy/repos?callback=ready
//  - create the ready function
//  - itearate through response.data array and console.log the name property

function tibi(obj) {
  // console.log(obj)
  obj.data.forEach(function(value){
    console.log(value.name);
  });
}
