# Objective:
#   To separate "Users" vs "Non-Users" in Mash-Cohort data (metagenomics data)
import pandas as pd
import os

#os.chdir("../..")


import PyPluMA
import PyIO
class SeparateMultiomicsPlugin:
    def input(self, inputfile):
       self.parameters = PyIO.readParameters(inputfile)
    def run(self):
       pass
    def output(self, outputfile):
       in_file = PyPluMA.prefix()+"/"+self.parameters["multiomics"]#"multiOmicsScaled.csv"
       metadata_file = PyPluMA.prefix()+"/"+self.parameters["metadata"]#"samplesMetadata.csv"

       out_users = outputfile+"_users.csv"#"MultiOmics_users.csv"
       out_NonUsers = outputfile+"_nonUsers.csv"#"MultiOmics_nonUsers.csv"
       out_copyUsers = outputfile+"_users.csv"#"MultiOmics_users.csv"
       out_copyNonUsers = outputfile+"_nonUsers.csv"#"MultiOmics_nonUsers.csv"


       metadata_df = pd.read_csv(metadata_file)
       metadata_df["group"] = metadata_df["Cocain_Use"]

       metadata_df = metadata_df[["group", "pilotpid"]]

       df = pd.read_csv(in_file)
       df = df.merge(metadata_df, how="right", on="pilotpid")

       df_users = df[df["group"]=="yes"]
       del df_users["group"]

       df_users.to_csv(out_users, index=False)
       df_users.to_csv(out_copyUsers, index=False)

       df_non_users = df[df["group"]=="no"]
       del df_non_users["group"]
       df_non_users.to_csv(out_NonUsers, index=False)
       df_non_users.to_csv(out_copyNonUsers, index=False)

