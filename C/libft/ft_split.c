/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: msornin <msornin@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/03 00:00:00 by msornin           #+#    #+#             */
/*   Updated: 2026/09/03 00:00:00 by msornin          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	ft_count_words(char const *s, char c)
{
	size_t	count;
	size_t	i;

	count = 0;
	i = 0;
	while (s[i] != '\0')
	{
		while (s[i] == c)
			i++;
		if (s[i] != '\0')
			count++;
		while (s[i] != '\0' && s[i] != c)
			i++;
	}
	return (count);
}

static size_t	ft_word_len(char const *s, char c)
{
	size_t	len;

	len = 0;
	while (s[len] != '\0' && s[len] != c)
		len++;
	return (len);
}

static void	ft_free_split(char **split, size_t used)
{
	while (used > 0)
	{
		used--;
		free(split[used]);
	}
	free(split);
}

static char	**ft_fill_split(char **split, char const *s, char c)
{
	size_t	i;
	size_t	word;
	size_t	len;

	i = 0;
	word = 0;
	while (s[i] != '\0')
	{
		while (s[i] == c)
			i++;
		if (s[i] != '\0')
		{
			len = ft_word_len(&s[i], c);
			split[word] = ft_substr(s, i, len);
			if (split[word] == NULL)
				return (ft_free_split(split, word), NULL);
			word++;
			i += len;
		}
	}
	split[word] = NULL;
	return (split);
}

char	**ft_split(char const *s, char c)
{
	char	**split;

	if (s == NULL)
		return (NULL);
	split = malloc((ft_count_words(s, c) + 1) * sizeof(char *));
	if (split == NULL)
		return (NULL);
	return (ft_fill_split(split, s, c));
}
