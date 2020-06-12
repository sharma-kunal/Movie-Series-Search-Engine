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

$('#main_cast').height($('.initial').height()-2*$('.detailsSwiper').height())
$('#production_cast').height($('.initial').height()-2*$('.detailsSwiper').height())
$('.details_content3').height($('.initial').height()-2*$('.detailsSwiper').height())
$('.details_content1').height($('.initial').height()-2*$('.detailsSwiper').height())

window.addEventListener('resize', function(e) {
    var currWidth = window.innerWidth;
    if (currWidth < 900) {
        console.log(currWidth);
        document.getElementsByClassName('images')[0].classList.remove('col-sm-8');
        document.getElementsByClassName('images')[0].classList.add('col-sm-12');
        $('.images').width(currWidth);
        $('.images').height(currWidth/2);
        $('#active-vertical').height(currWidth/2);
        $('.carousel-indicators').remove();
        if (currWidth < 400) {
            document.getElementById('active-vertical').style.maxWidth = "150px";
        } else {
            document.getElementById('active-vertical').style.maxWidth = "200px";
        }
        document.getElementById('active-vertical').style.display = "block";
        document.getElementById('active-vertical').style.margin = "auto";
//        $('#active-vertical').width(currWidth/2);
        $('#vertical').height(currWidth/2);
        if (currWidth < 400) {
            document.getElementById('vertical').style.maxWidth = "150px";
        } else {
            document.getElementById('vertical').style.maxWidth = "200px";
        }
        document.getElementById('vertical').style.display = "block";
        document.getElementById('vertical').style.margin = "auto";
//        $('#vertical').width(currWidth/2);
        var swiper3 = new Swiper('.watchOn', {
              slidesPerView: 3,
              spaceBetween: 30,
              pagination: {
                el: '.swiper-pagination',
                clickable: true,
              },
            });
        var swiper2 = new Swiper('.relatedMoviesSwiper', {
          slidesPerView: 2,
          spaceBetween: 20,
          pagination: {
            el: '.swiper-pagination',
            clickable: true,
          },
        });
    } else {
        document.getElementsByClassName('images')[0].classList.remove('col-sm-12');
        document.getElementsByClassName('images')[0].classList.add('col-sm-8');
    }
})
