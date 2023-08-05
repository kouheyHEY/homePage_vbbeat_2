/**
 * cssタグをheadタグ内に生成する
 * @param {string} href ファイルパス
 * @param {string} rel stylesheet
 * @param {string} type text/css
 */
function createLinkTag(href, rel, type) {
    var link = document.createElement("link");
    link.href = href;
    link.rel = rel;
    link.type = type;
    document.head.appendChild(link);
}