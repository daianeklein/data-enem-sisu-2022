# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8


# COMMAND ----------

# MAGIC %md # ENEM & SISU

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ## LIB'S

# COMMAND ----------




import pandas as pd



# COMMAND ----------

# MAGIC %md ## FUNCTIONS

# COMMAND ----------


# In[ ]:






# COMMAND ----------

# MAGIC %md ## DATA

# COMMAND ----------


# In[ ]:


path_enem_data = '/Users/daianeklein/Documents/DS/data-enem-sisu-2022/data/microdados_enem_2022/DADOS/MICRODADOS_ENEM_2022.csv'
enem_raw = pd.read_csv(path_enem_data, sep=';', encoding='latin-1')

enem_raw.shape


# In[ ]:


sisu_raw = pd.read_excel('../data/nota_corte_sisu_2023.xlsx',
                         'inscricao_2023_1')

sisu_raw.shape


# In[ ]:


sisu_df = sisu_raw.copy(deep=True)



# COMMAND ----------

# MAGIC %md ## DATA ANALYSIS

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### SISU DATA

# COMMAND ----------


# In[ ]:


sisu_df.head()


# In[ ]:


sisu_df.columns


# In[ ]:


sisu_df.head(20).T


# In[ ]:


sisu_df.groupby('SG_UF_CAMPUS')['NU_NOTACORTE'].mean()


# In[ ]:


sisu_df.groupby('SG_UF_CAMPUS')['NU_NOTACORTE'].median()

