# Système de Recommandation de Vins 

Prédiction des vins à recommander à chaque client à partir de 21 919 clients 
et 28 références vins, en exploitant les patterns d'achat croisés.

**Résultat** : moteur de recommandation déployé sur Streamlit → suggestions 
personnalisées pour chaque client + identification des vins similaires, 
réduisant le temps de recherche manuelle en CRM de plusieurs heures par semaine.

## Le problème

Un caviste souhaitait augmenter le panier moyen et la fidélisation. 
Le défi : exploiter uniquement l'historique d'achat (customer_id, wine_name, 
volume_in_ml) pour identifier quels vins proposer à quel client en leur proposant 
un moteur de recommandation

## Les données

- **21 919 clients uniques**
- **28 références vins**
- **Volume d'achat en ml** par transaction
- Source : l'entreprise / BigQuery 

## L'approche

1. **Agrégation** des achats par couple (client, vin)
2. **Normalisation** via `log1p` pour compresser les écarts de volume
3. **Encodage** des IDs avec `LabelEncoder`
4. **Matrice user-item creuse** (`scipy.sparse.csr_matrix`)
5. **Similarité cosinus** entre vins sur la base des acheteurs communs
6. **Recommandation client** : moyenne des similarités des vins déjà achetés, 
   en excluant ceux déjà consommés

## Stack

- **Python 3** — pandas, numpy
- **scikit-learn** 
- **Streamlit** — interface interactive déployée
- **BigQuery** — source de données
