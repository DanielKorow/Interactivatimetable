$(document).ready(function(){
$(".message a").click(function() {
    console.log("123");
  $("form").animate({ height: "toggle", opacity: "toggle" }, "slow");
});
});