
def bfs(CR, FR, s, t):
    #CR: Kapasite matrisi
    #FR: Akış matrisi
    #s: Kaynak düğüm
    #t: Hedef düğüm
   
    queue = [s]#baslangic dugumu s ile başladi
    paths = {s: []}#path sozlugu olusturuldu ve baglangic dugumu bos yol atandi. bu sozluk her dugumde en kisa yolu tutacak
    if s == t:
        return paths[s] #kaynak ve hedef dugumleri ayni ise fonksiyon bos yol donderir 
    while queue:#queuemuz bosalana kadar while dongusu donmeye devam eder
        u = queue.pop(0) #u dugumleri queuedan cikarilan degerleri isaret eder
        
        for v in range(len(CR)):# v = kapasite matrisi dugumleri
            if (CR[u][v] - FR[u][v] > 0) and v not in paths:#v dugumu daha once paths sozlugunde bulunmamissa yani bu dugume henuz bir yol atanmamissa bu sart saglanir.
                paths[v] = paths[u] + [(u, v)]#yeni yol ekle. paths[u]varolan yol, bu yola u,v eklenir. yeni yol paths[v]
                if v == t:#hedef dugum kontrolu
                    return paths[v]
                queue.append(v)#v dugumu daha once paths sozlugunde degılse ekle
    return None

def edmonds_karp_algorithm(entrances, exits, capacity):
    #bu fonksiyon kapasite matris giris dugumleri listesi ve cikis dugumleri list alir
    max_capacity = 9999#max kapasite sabiti
    n = len(capacity)# n= kapasite amtrisi boyutu
    s = n
    t = n + 1

   # bu artikli graf kapasite matrisinde her satira iki sutun ekler
    #1. cikis kapasitesi
    #2. giris kapasitesi
    residual_graph = [[capacity[u][v] for v in range(n)] for u in range(n)]
    for row in range(n):
        residual_graph[row].append(0)
        residual_graph[row].append(max_capacity if row in exits else 0)

    n += 2
    residual_graph.append([(max_capacity if x in entrances else 0) for x in range(n)])
    residual_graph.append([0] * n)

    FR = [[0] * n for i in range(n)]#tum degerleri 0 olan bir akis matrisi olusturulur

    
    paths = bfs(residual_graph, FR, s, t)#bfs algoritmasi ile artan yollar bulunur. her bir yol dugum cifti olarak ifade edilir
    while paths is not None:#artan yollarin tamami kullanildikca dongu devam eder
        flow = min(residual_graph[u][v] - FR[u][v] for u, v in paths)#bulunan yollarda min kapasiteye sahip baglantinin akis miktari hesaplama
        for u, v in paths:#bulunan her dugum cifti icin u.v girilir
            FR[u][v] += flow #baglantidaki akis miktari arttirilir
            FR[v][u] -= flow #yolun ters yonu icin baglantiya karsi cikis azaltiliyor

            if (v, u) in paths:#eger ters yonlu baglanti ise bu yonde kapasite arttirilir
                residual_graph[v][u] += flow
            else:
                residual_graph[u][v] -= flow

            if residual_graph[u][v] == 0:#eger baglantinin kapasitesi bittiyse ters yon kapasiteyi sifirla
                residual_graph[v][u] = 0

        paths = bfs(residual_graph, FR, s, t)#guncel artan yol bilgisi

   
    max_flow = sum(FR[s][i] for i in range(n))#max akis butun akislara giden yollarin toplanir

    return max_flow#hesaplanan max deger yazdirilir

#agdaki her bir kenarin kapasitesi
#bu matrisdeki her bir deger agdaki belirli bir kenarin tasiyabiilecegi max akis miktari
path = [
    [0, 10, 5, 15, 0],
    [0, 0, 0, 5, 10],
    [0, 0, 0, 15, 5],
    [0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0],
]

source = [0]
sink = [3]

max_flow = edmonds_karp_algorithm(source, sink, path)

print("Flow:",max_flow)
