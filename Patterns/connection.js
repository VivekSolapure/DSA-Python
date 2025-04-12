// const express= require("express")
// const server=express()

// server.use()

// server._


// async function getData() {
//     const url = "https://dummyjson.com/users";
//     const data= await fetch(url).then((data)=>{
//         return data.json()
//     })
    
//     const filteer= data.users.filter( user => user.university ==='Columbia University')
//     const finder= data.users.find( user => user.university ==='Columbia University')
//     console.log(finder);
    
//     // return filteer
//   }
  
// getData()

function outer() {
    let message = "Hello from outer";
  
    function inner() {
        let self=this
      console.log(self.message); // ✅ Can access outer function's variable
    }
  
    inner();
  }
  
  outer();
  // Output: "Hello from outer"
  // ❌ console.log(message); // Error: message is not defined (outside `outer()`)
  