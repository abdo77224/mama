import pandas as pd 
df=pd.read_csv('Housing.csv')#charger le fichier 
print(df)

print(df.head())#afficher 5 lignes premieres de dataframe
print(df.shape)#combien de lien et de colonne
print(df.columns)#afficher les noms de colonnes 
print(df.dtypes)#afficher les types de données
print(df.describe())
print(df.isnull())#vérification de valeur null
print("medianne de prix de maison est : ",df['price'].median())
print("medianne de prix de maison est : ",df['price'].mean())
print(df.isnull().sum())#compter combien valeur nulle dans chaque colonne
# Répartition pour chaque variable catégorielle
print("Répartition de 'mainroad':")
print(df['mainroad'].value_counts())
print(df['guestroom'].value_counts())
# Grouper par 'prefarea' et calculer le prix moyen
prix_moyen_par_quartier = df.groupby('prefarea')['price'].mean()
# Trier par prix moyen en ordre décroissant
prix_moyen_par_quartier = prix_moyen_par_quartier.sort_values(ascending=False)
# Afficher les 5 premiers quartiers
print("Les 5 quartiers avec les prix de vente moyens les plus élevés :")
print(prix_moyen_par_quartier.head())
# la moyenne des prix pour les maisons ayant
a=df[(df['airconditioning']=='yes') & (df['basement']=='yes') &(df['mainroad']=='yes')]['price'].mean()
print(a)
moyenne_prix_par_etages = df.groupby('stories')['price'].mean()

# Afficher les résultats
print("Moyenne des prix en fonction du nombre d'étages :")
print(moyenne_prix_par_etages)