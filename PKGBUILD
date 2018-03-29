# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-mplus-nocjk
pkgver=TESTFLIGHT_063
_pkgver=${pkgver/_/-}
pkgrel=1
pkgdesc="M+ Japanese outline fonts without CJK"
arch=('any')
url="http://mplus-fonts.osdn.jp/mplus-outline-fonts/index-en.html"
license=('custom')
depends=('fontconfig')
makedepends=('python' 'fontforge')
_mirror="jaist"
conflicts=('ttf-mplus')
source=(http://${_mirror}.dl.osdn.jp/mplus-fonts/62344/mplus-${_pkgver}.tar.xz
		keep-only-latin.py)
sha256sums=('149a5c97c35624d79ffb3cbbdd56559319085229acaf72b49b56adc5ede0979c'
            'dbf1c515940d47781a599f73e00ed518bcc50ae75a9482cd708bd194cbaecb79')

package() {
  cd ${srcdir}/mplus-${_pkgver}

  install -d ${pkgdir}/usr/share/fonts/TTF
  python ${srcdir}/remove-cjk.py
  install -m644 *.ttf ${pkgdir}/usr/share/fonts/TTF/

  install -D -m644 LICENSE_E \
          ${pkgdir}/usr/share/licenses/ttf-mplus/COPYING
}
