 # Maintainer: Your Name <youremail@domain.com>
pkgname=imgurupload
pkgver=1.0
pkgrel=1
pkgdesc="CLI for uploading images to imgur"
arch=('any')
url=""
license=('GPL')
groups=()
depends=('python2' 'python2-requests')
makedepends=('setuptools')
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=('imgur_upload.py' 'setup.py')
noextract=()
md5sums=() #generate with 'makepkg -g'

package() {
  cd "$srcdir"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}
md5sums=('3790e7100232cc429ba77e843dcc9e65'
         '922f3b52561cdd933ac856bd1374cd13')
