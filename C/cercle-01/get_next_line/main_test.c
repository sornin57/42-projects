/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main_test.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: msornin <msornin@student.42luxembourg.l    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/07 00:00:00 by msornin           #+#    #+#             */
/*   Updated: 2026/09/07 00:00:00 by msornin          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "get_next_line.h"

static void	print_line(int number, char *line)
{
	printf("line %d: %s\n", number, line);
	free(line);
}

int	main(void)
{
	int	fd;

	printf("found: %s\n", ft_strchr("hello\nbro", '\n'));
	fd = open("test.txt", O_RDONLY);
	if (fd == -1)
	{
		printf("Error: cannot open file\n");
		return (1);
	}
	print_line(1, get_next_line(fd));
	print_line(2, get_next_line(fd));
	print_line(3, get_next_line(fd));
	close(fd);
	return (0);
}
