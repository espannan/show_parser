if (document.images) {
	abo_on = new Image();	abo_on.src = "http://www.thefoxoakland.com/images/about_on.gif";
    joi_on = new Image();	joi_on.src = "http://www.thefoxoakland.com/images/join_on.gif";
    con_on = new Image();	con_on.src = "http://www.thefoxoakland.com/images/contact_on.gif";
	fhom_on = new Image();	fhom_on.src = "http://www.thefoxoakland.com/images/fhome_on.gif";
	fcal_on = new Image();	fcal_on.src = "http://www.thefoxoakland.com/images/fcal_on.gif";
	ftix_on = new Image();	ftix_on.src = "http://www.thefoxoakland.com/images/ftix_on.gif";
	fven_on = new Image();	fven_on.src = "http://www.thefoxoakland.com/images/fven_on.gif";
	fjoi_on = new Image();	fjoi_on.src = "http://www.thefoxoakland.com/images/fjoin_on.gif";
	fcon_on = new Image();	fcon_on.src = "http://www.thefoxoakland.com/images/fcon_on.gif";
}

//email
function draw_em(user,site) {
document.write('<a href=\"mailto:' + user + '@' + site + '.com\">');
document.write(user + '@' + site + '.com</a>');
}

//pop-up window code (for artist/show)
function openPop(cID){
	newWind=window.open
	('popartist.php?cID=' + cID,"popArtistWindow","status=no,toolbar=no,scrollbars=yes,resizable=no,width=475,height=550");
}

//pop-up window code (for any window)
function openPop2(url,w,h){
	newWind=window.open
	(url + ".html","openWindow","status=no,toolbar=no,scrollbars=yes,resizable=no,width=" + w + ",height=" + h);
}

//location code
function goToVenue(index){
	var cLoc = window.opener.location.href.toString();
	if (cLoc.indexOf('.cfm') > -1){
		nLoc = cLoc.substring(0,cLoc.lastIndexOf('/')) + '/venues.cfm?vid=' + index;
	}else if (cLoc.charAt(cLoc.length - 1) == '/'){
		nLoc = cLoc + 'venues.cfm?vid=' + index;
	}else{
		nLoc = cLoc + '/venues.cfm?vid=' + index;
	}
	window.opener.location.href = nLoc;
}

//drop-down menu code

if (!document.layers&&!document.all&&!document.getElementById)
event="test"
function showtip(current,e,text){

if (document.all||document.getElementById){
thetitle=text.split('<br>')
if (thetitle.length>1){
thetitles=''
for (i=0;i<thetitle.length;i++)
thetitles+=thetitle[i]
current.title=thetitles
}
else
current.title=text
}

else if (document.layers){
document.tooltip.document.write('<layer bgColor="white" style="border:1px solid black;font-size:12px;">'+text+'</layer>')
document.tooltip.document.close()
document.tooltip.left=e.pageX+5
document.tooltip.top=e.pageY+5
document.tooltip.visibility="show"
}
}
function hidetip(){
if (document.layers)
document.tooltip.visibility="hidden"
}

function change(id, newClass)
{
	identity=document.getElementById(id);
	identity.className=newClass;
}
