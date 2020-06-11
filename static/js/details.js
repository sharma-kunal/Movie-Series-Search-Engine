function details_tab(id) {
  if (id == "1") {
    document.getElementById("main_cast").style.visibility = "hidden";
    document.getElementById("production_cast").style.visibility = "hidden";
    document.getElementById("1").style.visibility = "visible";
    document.getElementById("2").style.visibility = "hidden";
    document.getElementById("3").style.visibility = "hidden";
    $('#swiper1').addClass('active-swiper');
    $('#swiper2').removeClass('active-swiper');
    $('#swiper3').removeClass('active-swiper');
  } else if (id == "2") {
    document.getElementById("main_cast").style.visibility = "visible";
    document.getElementById("production_cast").style.visibility = "hidden";
    document.getElementById("1").style.visibility = "hidden";
    document.getElementById("2").style.visibility = "visible";
    document.getElementById("3").style.visibility = "hidden";
    $('#swiper1').removeClass('active-swiper');
    $('#swiper2').addClass('active-swiper');
    $('#swiper3').removeClass('active-swiper');
    $('#swiper11').addClass('active-swiper');
    $('#swiper22').removeClass('active-swiper');
  } else {
    document.getElementById("main_cast").style.visibility = "hidden";
    document.getElementById("production_cast").style.visibility = "hidden";
    document.getElementById("1").style.visibility = "hidden";
    document.getElementById("2").style.visibility = "hidden";
    document.getElementById("3").style.visibility = "visible";
    $('#swiper1').removeClass('active-swiper');
    $('#swiper2').removeClass('active-swiper');
    $('#swiper3').addClass('active-swiper');
  }
}

function cast_tab(id) {
  if (id == "1") {
    document.getElementById("main_cast").style.visibility = "visible";
    document.getElementById("production_cast").style.visibility = "hidden";
    $('#swiper11').addClass('active-swiper');
    $('#swiper22').removeClass('active-swiper');
  } else {
    document.getElementById("main_cast").style.visibility = "hidden";
    document.getElementById("production_cast").style.visibility = "visible";
    $('#swiper11').removeClass('active-swiper');
    $('#swiper22').addClass('active-swiper');
  }
}

function readMore(id) {
    if (document.getElementById("readmore".concat(id)).getElementsByTagName("p")[0].innerHTML == "Read More") {
        document.getElementById("review".concat(id)).style.height = 'auto';
        document.getElementById("readmore".concat(id)).getElementsByTagName("p")[0].innerHTML = "Read Less"
    } else {
        document.getElementById("review".concat(id)).style.height = '45px';
        document.getElementById("readmore".concat(id)).getElementsByTagName("p")[0].innerHTML = "Read More"
    }
}

function recommendations(id, type) {
    window.location.href = "http://localhost:8090/movie?id=" + id + "&type=" + type;
}

// $("#swiper-slide-box").hover(function() {
//   $(this).css({"color": "white", "background": "black", "box-shadow": "0px 10px 40px #3e3c3c7a;"});
// }, function() {
//   $(this).css("background-color", "#2A2E43");
// });


// console.log($('.initial').height());
// console.log($('.detailsSwiper').height());

$('#main_cast').height($('.initial').height()-2*$('.detailsSwiper').height())
$('#production_cast').height($('.initial').height()-2*$('.detailsSwiper').height())
$('.details_content3').height($('.initial').height()-2*$('.detailsSwiper').height())
// castDivHeight = $('.details').height()-2*swiperContainerHeight;
// $('#main_cast').height(castDivHeight);
// $('#production_cast').height(castDivHeight);


// var swiperSlide = document.getElementsByClassName('detailsSwiper')[0].getElementsByClassName('swiper-slide');
// for(var index = 0; index< swiperSlide.length; index++) {
//   swiperSlide[index].addEventListener('mouseover',function(e) {
//       document.getElementById(index).style.backgroundColor = 'blue';
//   });
// }
