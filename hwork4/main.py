# HTML Nedir?

"""
Hiper Metin İşaretleme Dili(HTML) web sayfalarını oluşturmak için kullanılan standart metin işaretleme dilidir.
Dilin son sürümü HTML5'tir. HTML, bir programlama dili olarak tanımlanamaz.
Zira HTML kodlarıyla kendi başına çalışan bir program yazılamaz.
"""

# HTML Locators Nedir ?
"""
Locators(Konumlandırıcı), Selenium IDE'ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur.
Doğru elementin tanımlanması, otomasyon oluşturmanın ön koşuludur.
En yaygın locator çeşitleri;
ID
Name
ClassName
TagName
LinkText
CssSelector
Web sitelerinde tagname’ler bulunur.
Bu tagname’lerin sahip olduğu stil, name, id gibi attribute’ler vardır.
Selenium’un anlayacağı şekilde nesneleri web elementlere çevirirken ilk önce id’si ve name’i var mı?
diye bakılır yok ise CssSelector ve Xpath ile nesneyi bulmaya çalışırız.
"""

## Selenium'da Aksiyonlar
"""
Aksiyonlar:

click(): Bir öğeye tıklamak için kullanılır.
clear(): Bir öğenin içeriğini temizlemek için kullanılır.
submit(): Bir formu göndermek için kullanılır.
select_by_visible_text(): Bir dropdown öğesinde belirli bir metne tıklamak için kullanılır.
scroll(): Sayfayı aşağı veya yukarı kaydırmak için kullanılır.
switch_to_frame(): Bir iframe içine geçmek için kullanılır.
switch_to_window(): Bir pencereye geçmek için kullanılır.
back(): Önceki sayfaya gitmek için kullanılır.
forward(): Sonraki sayfaya gitmek için kullanılır.
refresh(): Sayfayı yenilemek için kullanılır.
"""

## Selenium'da İşlemler
"""
back(): Önceki sayfaya dönmek için kullanılır.
build(): Çalıştırılmak üzere inşa eder.
clear(): Metin kutusundaki mevcut metni silmek için kullanılır.
click(): Farenin geçerli konumuna tıklamak için kullanılır ya da istenilen alana sol tıklar.
clickAndHold(): Fareyi bulunduğu noktada basılı tutmayı sağlar.
contextClick(): Fare üzerinde sağ tıklama gerçekleştirir.
doubleClick(): Öğe üzerinde çift tıklama gerçekleştirir.
dragAndDrop(): İstenilen nesneyi istenilen yere sürükleyip bırakır.
forward(): Sonraki sayfaya gitmek için kullanılır.
keyDown(): Belirtilen tuşa basılı tutarak tuş kombinasyonu gerçekleştirir.
keyUp(): Basılı tuşu serbest bırakmadan yeni tuşa basmayı gerçekleştirir.
maximize_window(): Tam ekran yapmak için kullanılır.
moveToElement(): Fare işaretçisini öğenin merkezine kaydırır.
pause(): Testi duraklatır.
refresh(): Sayfayı yenilemek için kullanılır.
scroll(): Aşağı veya yukarı kaydırmak için kullanılır.
scrollByAmount(): İstenilen miktarda sayfanın kaydırılmasını sağlar.
scrollToElement(): Aranılan nesneye kadar kaydırılmasını sağlar.
select_by_visible_text(): Görünür metine tıklamak için kullanılır.
sendKeys(): İstenilen yere istenilen karakterlerin yazılmasını sağlar.
submit(): Teslim etmek/göndermek için kullanılır.
"""