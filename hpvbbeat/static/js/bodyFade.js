// ブラウザバック対策
window.onbeforeunload = function () {
    // IE用
};
window.onunload = function () {
    // IE以外用ここは空でOKです
};


// ローディング時の動き
$(window).on('load', function () {
    setTimeout(function () {
        // bodyに付けているfadeのクラスを取る
        $('body').removeClass('fade');
    }, 400);
});

$(function () {
    // ページ内リンク、target属性がない場合のaタグが押された時
    $('a:not([href^="#"]):not([target])').on('click', function (e) {
        e.preventDefault();
        link = $(this).attr('href');

        if (link !== '') {
            // bodyにフェードアウトさせるためのクラスを付与
            $('body').addClass('fadeout');
            setTimeout(function () {
                window.location = link;
            }, 400);
        }

        return false;
    })
});

$(function () {
    // フェードイン
    $('body').fadeIn(400);
});