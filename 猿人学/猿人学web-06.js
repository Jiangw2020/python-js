const encrypt = new (require('jsencrypt'))();
function parseKey(t) {
                    try {
                        var e = 0
                          , i = 0
                          , s = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/
                          , n = s.test(t) ? Hex.decode(t) : Base64.unarmor(t)
                          , r = ASN1.decode(n);
                        if (3 === r.sub.length && (r = r.sub[2].sub[0]),
                        9 === r.sub.length) {
                            e = r.sub[1].getHexStringValue(),
                            this.n = ae(e, 16),
                            i = r.sub[2].getHexStringValue(),
                            this.e = parseInt(i, 16);
                            var o = r.sub[3].getHexStringValue();
                            this.d = ae(o, 16);
                            var a = r.sub[4].getHexStringValue();
                            this.p = ae(a, 16);
                            var c = r.sub[5].getHexStringValue();
                            this.q = ae(c, 16);
                            var l = r.sub[6].getHexStringValue();
                            this.dmp1 = ae(l, 16);
                            var u = r.sub[7].getHexStringValue();
                            this.dmq1 = ae(u, 16);
                            var d = r.sub[8].getHexStringValue();
                            this.coeff = ae(d, 16)
                        } else {
                            if (2 !== r.sub.length)
                                return !1;
                            var p = r.sub[1]
                              , h = p.sub[0];
                            e = h.sub[0].getHexStringValue(),
                            this.n = ae(e, 16),
                            i = h.sub[1].getHexStringValue(),
                            this.e = parseInt(i, 16)
                        }
                        return !0
                    } catch (f) {
                        return !1
                    }
                }
                key = "-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDq04c6My441Gj0UFKgrqUhAUg+kQZeUeWSPlAU9fr4HBPDldAeqzx1UR99KJHuQh/zs1HOamE2dgX9z/2oXcJaqoRIA/FXysx+z2YlJkSk8XQLcQ8EBOkp//MZrixam7lCYpNOjadQBb2Ot0U/Ky+jF2p+Ie8gSZ7/u+Wnr5grywIDAQAB-----END PUBLIC KEY-----";
encrypt.setPublicKey(key)

var je = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
Le = "="
function be(t) {
    var e, i, s = "";
    for (e = 0; e + 3 <= t.length; e += 3)
        i = parseInt(t.substring(e, e + 3), 16),
        s += je.charAt(i >> 6) + je.charAt(63 & i);
    for (e + 1 == t.length ? (i = parseInt(t.substring(e, e + 1), 16),
    s += je.charAt(i << 2)) : e + 2 == t.length && (i = parseInt(t.substring(e, e + 2), 16),
    s += je.charAt(i >> 2) + je.charAt((3 & i) << 4)); (3 & s.length) > 0; )
        s += Le;
    return s
}

function z(t, e) {
     var i = e ? e + "|" + t : t;
     encrypt.setKey(key)
     console.log()
     return encodeURIComponent(encrypt.encrypt(i))
}
function r(param1, param2) {

    return be(z(param1, param2));
}
console.log(r(1758980596000,3))
console.log(be("dc93a8dd402b73c0de329aaac39e289aed730c4d59bef909dae589541cf5dc4365314ccd25ef3a6240715d2ea8e3d568e974bd684f20f98b412ada64e23c5d4d69695dbaf375d5316cca1b2379e1f084845abd048f3dc635e20693fbbef29e0e4ef4613e62dd93dd3dd33e0ef614ccb8d1d16d072ca5f0a131a730db9976685d"))
