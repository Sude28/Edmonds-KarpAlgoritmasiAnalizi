## Edmonds-KarpAlgoritmasiAnalizi
 # Problem
Bu proje, maksimum akış problemine odaklanmaktadır. Maksimum akış problemi, bir ağ 
üzerinde belirli bir kaynaktan hedefe maksimum akış miktarını bulmayı amaçlayan bir 
optimizasyon problemidir. Özellikle, bir ağdaki bağlantıların kapasiteleri ve kaynakların varlığı 
göz önüne alındığında, en etkili şekilde malzeme, bilgi veya kaynak akışının sağlanması 
hedeflenir.
# Genel Proje Açıklaması
Bu proje, Edmonds-Karp algoritmasını kullanarak maksimum akış problemine çözüm 
üretmeyi amaçlamaktadır. Maksimum akış problemi, bir ağ üzerinde belirli bir kaynaktan 
hedefe maksimum akış miktarını bulmayı hedefler. Bu tür problemler, taşıma ağları, iletişim 
ağları ve lojistik gibi birçok alanda uygulama bulur.
Bu proje, bir kapasite matrisini temsil eden veri kullanmaktadır. Bu matris, ağdaki düğümler 
arasındaki kapasiteleri gösterir.
Algoritmanın graf teorisi ve akış ağı problemlerine uygulanabilirliği, bilgisayar bilimi alanında 
kapsamlı bir anlayış geliştirmeye katkı sağlayabilir.
# Literatürü
Edmonds-Karp algoritması, maksimum akış problemlerini çözmek için kullanılan bir graf 
algoritmasıdır. Bu algoritma, Ford-Fulkerson algoritmasının bir türevidir ve en kısa artan yol 
bulma stratejisini kullanır.
Algoritma, bir ağ grafi üzerinde belirli bir kaynak ve hedef arasındaki maksimum akışı bulmayı 
amaçlar.Edmonds-Karp algoritmasının özelliği, artan yolun her zaman en kısa yol olmasıdır.
Mevcut akışı artırabilmek, en kısa yolunu bulmak için genişlik öncelikli arama (BFS) 
algoritmasını kullanır.
Edmonds-Karp algoritması, akışın güncellenmesi sırasında geriye akış adı verilen bir 
mekanizmayı kullanır. Geriye akış, akışın tersine gitmesine izin verir ve ağdaki kapasiteleri 
güncelleyerek, daha fazla artış yolunu keşfetme olasılığını artırır. Bu süreç, hedef düğüme 
ulaşılamayana kadar tekrarlanır.
Algoritmanın çalışma mantığı şu şekildedir:
 •Öncelikle, akış ağı bir Ford-Fulkerson algoritması kullanılarak en az bir akışa sahiptir.
 •Ardından, BFS algoritması kullanılarak, mevcut akışı artırabilecek en kısa yol bulunur.
 •Bu yol boyunca, akışın mümkün olduğunca fazla artırılmasına çalışılır.
 •Bu işlem, mevcut akışın maksimum akıya ulaştığına kadar tekrarlanır.
Veri iletimi, lojistik planlama, su kaynakları yönetimi, yazılım optimizasyonu, proje yönetimi, 
enerji dağıtımı, biyoinformatik ve oyun teorisi gibi çeşitli alanlarda uygulanabilir. EdmondsKarp algoritması, maksimum akış problemlerine pratik ve etkili çözümler sunarak, birçok 
endüstri ve disiplinde geniş bir kullanım yelpazesi sunar.
# Algoritma Analizi
Edmonds-Karp algoritmasının zaman karmaşıklığı O(VE^2) olarak ifade edilir. Burada V, 
düğüm sayısını, E ise kenar sayısını temsil eder. Bu karmaşıklık, her BFS adımında bir artış 
yolu bulma ve bu yolu kullanarak akışı güncelleme işlemlerini içerir. En kötü durumda, 
algoritma V kez BFS ve her BFS adımında en fazla E artış yolunu kontrol eder. Bu durumda, 
O(VE) adımda bir akış artırma işlemi gerçekleşir. Ancak, BFS adımının genellikle O(E) olduğu 
düşünülürse, toplam zaman karmaşıklığı O(VE^2) olur.
Edmonds-Karp algoritması, teorik olarak zaman karmaşıklığına sahip olabilir, ancak pratikte 
uygulama bağlamında hızlı ve etkili sonuçlar sağlar. Algoritmanın genişlik öncelikli arama 
kullanması, her adımda en kısa artış yolu bulma özelliğiyle önemli bir avantaja sahiptir. Bu 
özellik, algoritmanın genellikle düğüm ve kenar sayıları makul düzeyde olduğunda hızlı 
çalışmasını sağlar. Ancak, büyük ağlar veya yüksek sayıda düğüm ve kenar içeren 
problemlerde zaman karmaşıklığı nedeniyle performansı düşebilir.
# Algoritma Tasarımı
Bu kod, Edmonds-Karp algoritması kullanılarak bir akış ağındaki maksimum akışı bulmak için 
tasarlanmıştır. İşte kodunuzun çeşitli bölümlerinin açıklamaları:
1. BFS Fonksiyonu (bfs): Bu fonksiyon, genişlik öncelikli arama (BFS) kullanarak artış 
yollarını bulur. Verilen kapasite matrisi (CR), akış matrisi (FR), başlangıç düğümü (s) ve 
bitiş düğümü (t) ile birlikte, BFS kullanarak artış yollarını tespit eder.
2. Edmonds-Karp Algoritması (edmonds_karp_algorithm): Bu fonksiyon, akış ağındaki 
maksimum akışı bulmak için Edmonds-Karp algoritmasını uygular. Ağa giriş ve çıkış 
düğümleri eklenerek bir artıklık grafiği oluşturulur. Ardından, BFS fonksiyonu 
kullanılarak artış yolları bulunur ve akış matrisi güncellenir. Bu işlem, artış yolu 
bulunamayana kadar devam eder.
 İlk olarak, giriş ve çıkış düğümleri eklenir ve bir artıklık grafiği oluşturulur.
 BFS ile artış yolları bulunur ve bu yollar üzerinde akış güncellemeleri yapılır.
 BFS ile artış yolu bulunamayana kadar işlem devam eder.
 Sonuç olarak, maksimum akış hesaplanır ve bu değer döndürülür.
3. Akış ve Kapasite Güncellemeleri:
 Akış matrisi (FR) ve artıklık grafiği güncellenir.
 Akış matrisi, artış yolu boyunca minimum kapasiteye göre güncellenir.
 Artıklık grafiğindeki kapasiteler ve ters yöndeki kapasiteler güncellenir.
4. Graf Güncellemeleri:
 Akış matrisine göre artıklık grafiği güncellenir.
 Akışın tamamen kullanıldığı yollar kaldırılır.
5. Maksimum Akış Hesaplama:
 Maksimum akış, başlangıç düğümünden çıkış düğümüne giden toplam akış 
olarak hesaplanır.
# Sonuçlar
•Algoritma, BFS kullanarak maksimum akışı artırır ve bu sayede maksimum akış problemi 
çözülür.
•Algoritmanın karmaşıklığı genellikle O(V * E^2) olarak ifade edilir, burada V düğüm sayısını, 
E kenar sayısını temsil eder.
•Verilen kapasite matrisine dayanarak, kaynak ve hedef düğümleri arasındaki maksimum 
akış miktarını bulur.
•Algoritma, artırılmış yolların BFS kullanılarak bulunması ve akışın güncellenmesi 
prensiplerine dayanır

