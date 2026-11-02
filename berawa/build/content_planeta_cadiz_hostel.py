# Contenido de la demo Planeta Cádiz Hostel (Cádiz) (es/en/fr/de). Hechos de planetacadizhostel.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes; sin precios.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hostel real.','en':' Images are illustrations and do not show the actual hostel.','fr':' Les images sont des illustrations et ne montrent pas l’auberge réelle.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hostel.'}
H={'es':['Dobles','Familiares','Para compartir'],'en':['Doubles','Family rooms','Shared rooms'],'fr':['Doubles','Familiales','À partager'],'de':['Doppelzimmer','Familienzimmer','Mehrbettzimmer']}
RD={
'es':['Doble Económica y Doble Deluxe, para parejas.','Deluxe para 4 personas (también con terraza) y para 6 personas.','De 4, 6 y 10 personas, para grupos de amigos o mochileros.'],
'en':['Economy Double and Deluxe Double, for couples.','Deluxe rooms for 4 people (also with a terrace) and for 6 people.','For 4, 6 and 10 people, for groups of friends or backpackers.'],
'fr':['Double Économique et Double Deluxe, pour les couples.','Deluxe pour 4 personnes (aussi avec terrasse) et pour 6 personnes.','De 4, 6 et 10 personnes, pour groupes d’amis ou routards.'],
'de':['Economy-Doppelzimmer und Deluxe-Doppelzimmer, für Paare.','Deluxe für 4 Personen (auch mit Terrasse) und für 6 Personen.','Für 4, 6 und 10 Personen, für Freundesgruppen oder Backpacker.']}
ART={
'hero':('waves',9901,['#14303f','#e8b56a','#f6dcaa','#2f6f86','#245a6e','#123444']),
'intro':('arches',9902,['#eef3f4','#f9f7f2','#2f6f86','#245a6e','#123444']),
'r1':('arches',9911,['#eef1f2','#d39b57','#2f6f86','#245a6e','#123444']),
'r2':('columns',9912,['#f0ece4','#f9f5ee','#b5602f','#8a4a1e','#4a2810']),
'r3':('skyline',9913,['#14303f','#e0aa64','#f4d7a6','#3f7f96','#2f677c','#173a48']),
'g1':('waves',9921,['#1a3a4a','#edbd83','#f6deb5','#3c7a90','#2c6478','#1a3a48']),
'g2':('arches',9922,['#f2ede4','#f9f5ee','#b5602f','#8a4a1e','#4a2810']),
'g3':('skyline',9923,['#e8eef0','#f1e2c3','#d6a160','#7d9aa6','#5a7884','#38525c']),
'g4':('columns',9924,['#14303f','#e8b56a','#f6dcaa','#2f6f86','#245a6e','#123444'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Planeta Cádiz Hostel · Hostel en el centro histórico de Cádiz',see_rooms='Ver las habitaciones',hero_k='Cádiz · Calle Montañés 16',hero_t='Un hostel en una casa señorial del siglo XIX',hero_s='En pleno casco histórico de Cádiz, con habitaciones dedicadas a la ciudad.',
 intro_t='Historia gaditana y comodidad moderna',intro_p1='Situado en el corazón de Cádiz, en pleno centro histórico, el hostel ocupa una casa señorial del siglo XIX que fusiona la historia con lo moderno.',
 intro_p2='Aire acondicionado, literas con luz y enchufe propios, kiosco de autocheck-in las 24 horas y un diseño gaditano de la mano del artista Jonatan Alcina.',
 stats=['Casa del siglo XIX','Recepción 24 horas','Terraza','Wifi gratis'],nav_rooms='Habitaciones',rooms_t='Vengas con quien vengas',rooms_s='Dobles, familiares y para compartir.',
 svcs=['Desayunos','Cocina comunitaria','Terraza y bar','Lavandería','Alquiler de bicicletas','Ascensor'],
 around_s='A 200 m de la Torre Tavira, a 350 m de la Catedral de Santa Cruz y a 1 km de la playa de La Caleta.',
 loc_p='Calle Montañés 16 · Cádiz, en pleno casco histórico.',
 chips=['¿Qué habitaciones tenéis?','¿Hay desayuno?','¿Qué hay cerca?','¿Cómo reservo?']),
'en':dict(title='Planeta Cádiz Hostel · Hostel in the historic centre of Cádiz',see_rooms='See the rooms',hero_k='Cádiz · Calle Montañés 16',hero_t='A hostel in a 19th-century manor house',hero_s='Right in the old town of Cádiz, with rooms themed on the city.',
 intro_t='Cádiz history and modern comfort',intro_p1='Located in the heart of Cádiz, right in the historic centre, the hostel occupies a 19th-century manor house that blends history with the modern.',
 intro_p2='Air conditioning, bunk beds with their own light and socket, a 24-hour self check-in kiosk and Cádiz-style design by the artist Jonatan Alcina.',
 stats=['19th-century house','24-hour reception','Terrace','Free wifi'],nav_rooms='Rooms',rooms_t='Whoever you come with',rooms_s='Doubles, family rooms and shared rooms.',
 svcs=['Breakfast','Shared kitchen','Terrace and bar','Laundry','Bike rental','Lift'],
 around_s='200 m from the Torre Tavira, 350 m from the Cathedral of Santa Cruz and 1 km from La Caleta beach.',
 loc_p='Calle Montañés 16 · Cádiz, right in the old town.',
 chips=['Which rooms do you have?','Is there breakfast?','What is nearby?','How do I book?']),
'fr':dict(title='Planeta Cádiz Hostel · Auberge dans le centre historique de Cadix',see_rooms='Voir les chambres',hero_k='Cadix · Calle Montañés 16',hero_t='Une auberge dans une maison de maître du XIXe siècle',hero_s='En plein centre historique de Cadix, avec des chambres dédiées à la ville.',
 intro_t='Histoire gaditane et confort moderne',intro_p1='Située au cœur de Cadix, en plein centre historique, l’auberge occupe une maison de maître du XIXe siècle qui mêle histoire et modernité.',
 intro_p2='Climatisation, lits superposés avec lumière et prise individuelles, borne d’auto-enregistrement 24 h/24 et un design gaditan signé par l’artiste Jonatan Alcina.',
 stats=['Maison du XIXe siècle','Réception 24 h/24','Terrasse','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Quel que soit votre compagnon de voyage',rooms_s='Doubles, familiales et à partager.',
 svcs=['Petits-déjeuners','Cuisine commune','Terrasse et bar','Laverie','Location de vélos','Ascenseur'],
 around_s='À 200 m de la Torre Tavira, à 350 m de la cathédrale de Santa Cruz et à 1 km de la plage de La Caleta.',
 loc_p='Calle Montañés 16 · Cadix, en plein centre historique.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un petit-déjeuner ?','Qu’y a-t-il à proximité ?','Comment réserver ?']),
'de':dict(title='Planeta Cádiz Hostel · Hostel in der Altstadt von Cádiz',see_rooms='Zimmer ansehen',hero_k='Cádiz · Calle Montañés 16',hero_t='Ein Hostel in einem Herrenhaus aus dem 19. Jahrhundert',hero_s='Mitten in der Altstadt von Cádiz, mit Zimmern, die der Stadt gewidmet sind.',
 intro_t='Geschichte von Cádiz und moderner Komfort',intro_p1='Im Herzen von Cádiz, mitten in der Altstadt, befindet sich das Hostel in einem Herrenhaus aus dem 19. Jahrhundert, das Geschichte und Moderne verbindet.',
 intro_p2='Klimaanlage, Etagenbetten mit eigenem Licht und eigener Steckdose, ein Self-Check-in-Kiosk rund um die Uhr und Design aus Cádiz vom Künstler Jonatan Alcina.',
 stats=['Haus aus dem 19. Jh.','24-Stunden-Rezeption','Terrasse','Kostenloses WLAN'],nav_rooms='Zimmer',rooms_t='Egal, mit wem Sie kommen',rooms_s='Doppel-, Familien- und Mehrbettzimmer.',
 svcs=['Frühstück','Gemeinschaftsküche','Terrasse und Bar','Wäscherei','Fahrradverleih','Aufzug'],
 around_s='200 m vom Torre Tavira, 350 m von der Kathedrale Santa Cruz und 1 km vom Strand La Caleta entfernt.',
 loc_p='Calle Montañés 16 · Cádiz, mitten in der Altstadt.',
 chips=['Welche Zimmer gibt es?','Gibt es Frühstück?','Was gibt es in der Nähe?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://booking.avirato.com/?code=44454701'
BOOK=dict(mode='engine',url={l:RB+'&lang='+l for l in ('es','en','fr','de')})
D=dict(name='Planeta Cádiz Hostel',ac='#14303f',ac2='#2f6f86',ac2_a11y='#245a6e',book=BOOK,around=['Torre Tavira','Catedral de Cádiz'],foot=FOOT,
 address='Calle Montañés 16 · Cádiz',phones=['+34 956 21 07 02'],emails=['reservas@planetacadizhostel.com'],maps='Planeta Cádiz Hostel, Calle Montañés 16, Cádiz',t=T)
META=dict(repo='demo-planeta-cadiz-hostel',name='Planeta Cádiz Hostel',legal_name='CADIZ PLANET SL (aviso legal / política de privacidad de su web)',registry_ids=['B72369416','H/CA/01473'],
 url='https://www.planetacadizhostel.com/',domain='planetacadizhostel.com',municipality='Cádiz',province='Cádiz',sector='hostel en una casa del siglo XIX del casco histórico de Cádiz',
 read_at='2026-10-30T10:57:00+01:00',created_at='2026-10-30T10:57:00+01:00',built_at='2026-10-30T11:15:00+01:00',audit_date='2026-10-30T10:51:57+01:00',
 rating=dict(value=4.1,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Planeta+Cadiz+Hostel/@36.5316834,-6.2961478,17z/data=!4m9!3m8!1s0xd0dd1609e929111:0x8a05aa46790f3aff!5m2!4m1!1i2!8m2!3d36.5316834!4d-6.2961478!16s%2Fg%2F11j3pnt509'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (Avirato, code 44454701, enlazado desde los botones RESERVAR de sus habitaciones), HTTP 200 comprobado el 30/10/2026 con lang es/en/fr/de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Hay desayuno?','K02'),('¿Tenéis cocina?','K03'),('¿Hay wifi?','K04'),('¿La recepción está abierta 24 horas?','K05'),('¿Hay terraza?','K06'),('¿Qué hay cerca?','K07'),('¿Dónde está el hostel?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Tenéis lavandería?','K10'),('¿Alquiláis bicicletas?','K11'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Is there breakfast?','K02'),('Is there a kitchen?','K03'),('Is there wifi?','K04'),('Is reception open 24 hours?','K05'),('Is there a terrace?','K06'),('What is nearby?','K07'),('Where is the hostel?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('Do you have laundry?','K10'),('Do you rent bikes?','K11'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Y a-t-il un petit-déjeuner ?','K02'),('Y a-t-il une cuisine ?','K03'),('Y a-t-il le wifi ?','K04'),('La réception est-elle ouverte 24 h/24 ?','K05'),('Y a-t-il une terrasse ?','K06'),('Qu’y a-t-il à proximité ?','K07'),('Où se trouve l’auberge ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Avez-vous une laverie ?','K10'),('Louez-vous des vélos ?','K11'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Gibt es Frühstück?','K02'),('Gibt es eine Küche?','K03'),('Gibt es WLAN?','K04'),('Ist die Rezeption rund um die Uhr geöffnet?','K05'),('Gibt es eine Terrasse?','K06'),('Was gibt es in der Nähe?','K07'),('Wo liegt das Hostel?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Gibt es eine Wäscherei?','K10'),('Verleihen Sie Fahrräder?','K11'),('Was kostet eine Nacht?',None),('Haben Sie ein Schwimmbad?',None)]}
