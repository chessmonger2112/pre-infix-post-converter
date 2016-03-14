$(function(){
  console.log("test");
  var from = "";
  var to = "";
  var expressionInput = "";

  $(".from").click(function(){
    var butt = this.id;
    var that = this;
    console.log(`From: ${this.id + that.innerHTML}`)
    $("#commandContainer").show();
    from = that.innerHTML;
    $("#conversionType").val(from);
    $(".from").css("color","black");
    $(this).css("color","red");
  });

  $(".to").click(function(){
    var butt = this.id;
    var that = this;
    console.log(`To: ${this.id + that.innerHTML}`);
    $("#calculate").show();
    to = that.innerHTML;
    $("#to").text(to);
    $("#conversionType2").val(to);
    $("#from").text(from);
    $("#to").text(to);
    $("#fromTo").show();
    $(".to").css("color","black");
    $(this).css("color","red");
    var expressionInput = $("#inputCommand").val();
    $("#expression").val(expressionInput)
  });
})
