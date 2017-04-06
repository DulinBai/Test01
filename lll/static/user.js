var username="王宝强";
var gender="男";
var job="校长";
var unit="西安电子科技大学";
var field="域内";

var filename="文件01";
var filesize=1042;
var modify="2017-03-20 22:32";
var authority="读写操作";

/*输入用户表格信息*/
document.write('<table class="tab-user">');
document.write('<caption id="tab1">用户信息</caption>');

document.write('<tr>');
document.write('<th>'+"用户名"+'</th><td>'+Piece_dict.id_num+'</td>');
document.write('</tr>');
document.write('<tr>');
document.write('<th>'+"性别"+'</th><td>'+Piece_dict.gender+'</td>');
document.write('</tr>');
document.write('<tr>');
document.write('<th>'+"职务"+'</th><td>'+Piece_dict.position+'</td>');
document.write('</tr>');
document.write('<tr>');
document.write('<th>'+"工作单位"+'</th><td>'+Piece_dict.unit+'</td>');
document.write('</tr>');
document.write('<tr>');
document.write('<th>'+"域"+'</th><td>'+Piece_dict.partjob+'</td>');
document.write('</tr>');

document.write('</table >');

/*输入文件表格信息*/
document.write('<table class="tab-file">');
document.write('<caption id="tab2">文件信息</caption>');

document.write('<tr>');
document.write('<th>'+"文件名"+'</th><th>'+"文件大小"+'</th><th id="th01">'+"修改时间"+'</th><th>'+"权限"+'</th>');
document.write('</tr>');
document.write('<tr>');
document.write('<td>'+filename+'</td><td>'+filesize+'</td><td id="th02">'+modify+'</td><td>'+authority+'</td>');
document.write('</tr>');

document.write('</table >');
