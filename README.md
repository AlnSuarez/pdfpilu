
# Datagram's API

The following api is for datagram, shows how the objects should look like for each of the possible routes to which you can make requests


## API Reference

#### Create a template for Club Puebla

```http
  Post /api/club-puebla/template
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Body object` | `object` | Below is an example of how objects must be sent to obtain a successful response.|

#### Example of how to create an object:

```json
{
    "list": [
        {
            "name": "ALAN SUAREZ",
            "position": "JUGADOR",
            "color": "permanente",
            "access": {
                "one": "ex",
                "two": "ca",
                "three": "tr"
            }
        },
        {
            "name": "BENJA PADILLA",
            "position": "JUGADOR",
            "color": "rosa",
            "access": {
                "one": "ex",
                "two": "ca",
                "three": "tr"
            }
        }
    ]
}

```

#### Create an order for PILU

```http
  Post /api/pilu/pdf
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Body object` | `object` | Below is an example of how objects must be sent to obtain a successful response.|

#### Example of how to create an object:

```json
{
    "address": "colonia las palmas",
    "phone": "124342345",
    "city": "puebla",
    "state": "puebla",
    "zipcode": 72374,
    "website": "www.pilu.com",
    "pedidos": [
        {
            "prenda": " esto es una prueba",
                "tela": "cardian askdkasdaksda",
                "bordado": "Frente: Izquierda Tipode bordado: Directo ala PrendaComentarios: DIPASAColor: VERDE" },
            {
            "prenda": "VESTIR PARA CABALLERO MANGALARGA Tallas: 30/1 piezas 34/10 piezas36/12 piezas 40/4 piezas 42/3 piezasPARTIDA 1--------Camisa de vestir mangalarga para Caballero, en tela Oxford Italiano(KAIKALA) 60% algodón / 40% poliéster, encolor BLANCO; Con cuello, pie de cuello ybotón down; en el frente superior izquierdouna bolsa terminación en pico CONSEPARACIÓN PARA LAPICEROCARGADA A LA PARTE INTERNA DE LAPRENDA; Manga larga puño redondo, ojal ybotón, bebedero en forma de flecha y dostablones cargados al bebedero; Espalda condoble bata y tablón en parte central de laespalda baja; CONTRASTES EN PIE DECUELLO INTERNO, PUÑOS INTERNOS YALETILLA BOTONERA EN TELA OXFORDITALIANO (KALTEX) EN COLOR AZULMARINO. ------------ Bordado directo a laprenda logo DIPASA en el frente superiorizquierdo arriba de la bolsa.",
                "tela": "Tela: KAIKALAOXFORD ITALIANO60% ALG. / 40% POL.BLANCO Color:BLANCO Composición: 60/40ALG-PO",
                "bordado": "Frente: Izquierda Tipode bordado: Directo ala PrendaComentarios: DIPASAColor: VERDE" }
                
        ]
}

```

