# Install and load necessary packages
if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
if (!requireNamespace("Rtsne", quietly = TRUE)) install.packages("Rtsne")
if (!requireNamespace("umap", quietly = TRUE)) install.packages("umap")
if (!requireNamespace("cowplot", quietly = TRUE)) install.packages("cowplot")
library(tidyverse)
library(ggplot2)
library(Rtsne)
library(umap)
library(cowplot)




# Load the iris dataset
myData <- read.csv('PCA/covid_PCA_df_parameter_asia.csv', header = T) #must be specific format for dataframehead(myData, n=3)
m_myData <- myData %>%
  #filter(Species %in% c("Cred","Cpurple","Cyellow","Cskyb","Cgreen","Corange","Cblue","Czamong","private")) %>%
  drop_na() %>%
  select(Species,mut,starts_with('p')) %>%
  mutate(ID=row_number())


# PCA
pca <- prcomp(m_myData[, 3:19], center = TRUE, scale = TRUE)
pca_df <- data.frame(PC1 = pca$x[, 1], PC2 = pca$x[, 2], Species = m_myData$Species)

# PCA + t-SNE
pca_tsne <- Rtsne(pca$x[, 1:2], check_duplicates = FALSE, pca = FALSE, perplexity = 30, theta = 0.5)
pca_tsne_df <- data.frame(PC1 = pca_tsne$Y[, 1], PC2 = pca_tsne$Y[, 2], Species = m_myData$Species)

# t-SNE
tsne <- Rtsne(m_myData[, 3:19], check_duplicates = FALSE, pca = TRUE, perplexity = 30, theta = 0.5)
tsne_df <- data.frame(TSNE1 = tsne$Y[, 1], TSNE2 = tsne$Y[, 2], Species = m_myData$Species)

# UMAP
umap_res <- umap(m_myData[, 3:19], n_neighbors = 15, min_dist = 0.1, metric = "euclidean")
umap_df <- data.frame(UMAP1 = umap_res$layout[, 1], UMAP2 = umap_res$layout[, 2], Species = m_myData$Species)



# Visualization functions
plot_pca <- ggplot(pca_df, aes(x = PC1, y = PC2, color = Species)) +
  geom_point(aes(color=Species),size=4) +
  theme_bw(base_size=20) +
  scale_color_manual(name = "Species",
                     labels = c("Cred","Cpurple","Cyellow","Cskyb","Cgreen","Corange","Cblue","Czamong","private"),
                     values = c("#3A63A3", "#4A9245", "orange", "purple", "red", "skyblue", "#B8BF49", "#BE4783", "gray"))+
  geom_point() +
  theme_minimal() +
  labs(title = "PCA", x = "PC1", y = "PC2")

plot_pca_tsne <- ggplot(pca_tsne_df, aes(x = PC1, y = PC2, color = Species)) +
  geom_point(aes(color=Species),size=4) +
  theme_bw(base_size=20) +
  scale_color_manual(name = "Species",
                     labels = c("Cred","Cpurple","Cyellow","Cskyb","Cgreen","Corange","Cblue","Czamong","private"),
                     values = c("#3A63A3", "#4A9245", "orange", "purple", "red", "skyblue", "#B8BF49", "#BE4783", "gray"))+
  geom_point() +
  theme_minimal() +
  labs(title = "PCA + t-SNE", x = "t-SNE1", y = "t-SNE2")

plot_tsne <- ggplot(tsne_df, aes(x = TSNE1, y = TSNE2, color = Species)) +
  geom_point(aes(color=Species),size=4) +
  theme_bw(base_size=20) +
  scale_color_manual(name = "Species",
                     labels = c("Cred","Cpurple","Cyellow","Cskyb","Cgreen","Corange","Cblue","Czamong","private"),
                     values = c("#3A63A3", "#4A9245", "orange", "purple", "red", "skyblue", "#B8BF49", "#BE4783", "gray"))+
  geom_point() +
  theme_minimal() +
  labs(title = "t-SNE", x = "t-SNE1", y = "t-SNE2")

plot_umap <- ggplot(umap_df, aes(x = UMAP1, y = UMAP2, color = Species)) +
  geom_point(aes(color=Species),size=4) +
  theme_bw(base_size=20) +
  scale_color_manual(name = "Species",
                     labels = c("Cred","Cpurple","Cyellow","Cskyb","Cgreen","Corange","Cblue","Czamong","private"),
                     values = c("#3A63A3", "#4A9245", "orange", "purple", "red", "skyblue", "#B8BF49", "#BE4783", "gray"))+
  geom_point() +
  theme_minimal() +
  labs(title = "UMAP", x = "UMAP1", y = "UMAP2")

# Combine plots
combined_plot <- plot_grid(plot_pca, plot_pca_tsne, plot_tsne, plot_umap, nrow = 2)

combined_plot



