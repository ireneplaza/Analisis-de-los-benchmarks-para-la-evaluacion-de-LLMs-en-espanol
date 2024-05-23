import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")

pater_noster = enc.encode("Vater Unser im Himmel! Geheiligt werde dein Name. Dein Reich komme. Dein Wille geschehe, wie im Himmel, so auf Erden. Unser tägliches Brot gib uns heute. Und vergib uns unsere Schuld, wie auch wir vergeben unseren Schuldigern. Und führe uns nicht in Versuchung, sondern erlöse uns von dem Bösen. Denn dein ist das Reich und die Kraft und die Herrlichkeit. In Ewigkeit. Amen.")

print (pater_noster)
print(len(pater_noster))

#https://es.askingbox.com/informacion/padre-nuestro-en-otros-idiomas#indonesio