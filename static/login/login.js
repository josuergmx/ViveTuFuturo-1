$(function () {
    var body = $('body');
    var backgrounds = [
      'url(../images/login/login1.jpg) no-repeat center center fixed', 
      'url(../images/login/login2.jpg) no-repeat center center fixed',
      'url(../images/login/login3.jpg) no-repeat center center fixed'];
    var current = 0

    function nextBackground() {
        body.css(
            'background',
        backgrounds[current = ++current % backgrounds.length]);

        setTimeout(nextBackground, 5000);
    }
    setTimeout(nextBackground, 5000);
    body.css('background', backgrounds[0]);
});