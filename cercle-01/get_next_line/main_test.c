#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "get_next_line.h"

int	main(void)
{
	int		fd;
	char	*line;
	char	*found;

	found = ft_strchr("hello\nbro", '\n');
	printf("found: %s\n", found);

	fd = open("test.txt", O_RDONLY);
	if (fd == -1)
	{
		printf("Error: cannot open file\n");
		return (1);
	}
	line = get_next_line(fd);
	printf("line 1: %s\n", line);
	free(line);

	line = get_next_line(fd);
	printf("line 2: %s\n", line);
	free(line);

	line = get_next_line(fd);
	printf("line 3: %s\n", line);
	free(line);
	close(fd);
	return (0);
}
