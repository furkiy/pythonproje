import streamlit as st

def hesapla_birikim(ev_fiyati,kira,birikim_miktari,kredi_suresi,pesinat_orani,hedef_ev_sayisi):
    aylik_birikim=birikim_miktari
    toplam_birikim=0
    ev_sayisi=0
    toplam_kira_getirisi=0
    ev_fiyati_pesinat=ev_fiyati*pesinat_orani

    while ev_sayisi<hedef_ev_sayisi:
        toplam_birikim+=aylik_birikim
        
        if toplam_birikim>=ev_fiyati_pesinat:
            toplam_birikim-=ev_fiyati_pesinat
            toplam_kira_getirisi+=kira
            ev_sayisi+=1
            
            kalan_kredi=ev_fiyati-ev_fiyati_pesinat
            aylik_kredi_odemesi=kalan_kredi/(kredi_suresi*12)
            aylik_birikim+=kira-aylik_kredi_odemesi

    return toplam_birikim,toplam_kira_getirisi

def main():
    st.title("Ev Birikimi")
    
    ev_fiyati = st.number_input("Evin Fiyatı:",min_value=0)
    kira = st.number_input("Kira Bedeli:",min_value=0)
    birikim_miktari = st.number_input("Aylık Birikim Miktarı:",min_value=0)
    kredi_suresi = st.number_input("Kredi Süresi Kaç Yıl:",min_value=1)
    pesinat_orani = st.slider("Peşinat Oranı:", 0.0, 1.0, 0.2,step=0.01)
    hedef_ev_sayisi = st.number_input("Hedeflenen Ev Sayısı:",min_value=1)

    if st.button("Hesapla"):
        toplam_birikim, kira_getirisi = hesapla_birikim(ev_fiyati, kira, birikim_miktari, kredi_suresi, pesinat_orani, hedef_ev_sayisi)
        st.success(f"Hedeflenen ev sayısı için ulaşılması gereken birikim miktarı: {toplam_birikim:.2f} ₺, toplam kira getirisi: {kira_getirisi:.2f} ₺")

if __name__ == "__main__":
    main()