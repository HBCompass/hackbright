
var getText = document.getElementById("get-text");
getText.addEventListener('click',function(e){
    e.preventDefault();
    var theDiv = document.getElementById("text-box-replace").innerHTML = "World";
    
    //debugger;
    
});



var getColor = document.getElementById("get-color");
getColor.addEventListener('click', function(e) {
    e.preventDefault();
    var greenDiv = document.getElementById("text-box-color");
    greenDiv.style.backgroundColor = 'red';
    greenDiv.innerHTML = "I am the color red!";
});



var getMelon = document.getElementById("get-melon");
getMelon.addEventListener('click', function(e) {
    e.preventDefault();
    var melonPic = document.getElementById("melon-box").getElementsByTagName("img")[0];
    melonPic.setAttribute('src', "http://static.parastorage.com/media/d02841_c0ae158ec45f4d2082ce1e2997b18509.jpg_256");
});














// var getAwesome = document.getElementById("be-awesome");
// getAwesome.addEventListener('click', function(e)  {
//     e.preventDefault();
//     function toggle(){ var awesomeBox = document.getElementById("awesome-box");
//     awesomeBox = awesomeBox.elementNodeReference.classList;
//     span.classList.remove("hidden");
// }
// });



var getAwesome = document.getElementById("be-awesome");
var getSpan = document.getElementById("awesome-box");
function toggle() {
    getSpan.classList.toggle('hidden');
}
getAwesome.addEventListener('click',toggle, false);
