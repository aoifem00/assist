function getFormData(){
  var name=document.getElementById('username').value;
  var password=document.getElementById('password').value;

  alert(name);
  var fs=require("fs");
  var obj={name:password};
  fs.writeFile("./login.json", JSON.stringify(obj), (err)=>
{
  if(err){
    alert("Error");
    return;
  }
}

}
function myFunc(){
  alert("Hello world");
}
