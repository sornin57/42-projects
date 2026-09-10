#include "codexion.h"

static int	is_number(char *str)
{
	int	i;

	i = 0;
	if (!str || str[0] == '\0')
		return (0);
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			return (0);
		i++;
	}
	return (1);
}

static int	read_positive(char *str)
{
	if (is_number(str) == 0)
		return (-1);
	return (atoi(str));
}

static int	read_scheduler(char *str)
{
	if (strcmp(str, "fifo") == 0)
		return (0);
	if (strcmp(str, "edf") == 0)
		return (1);
	return (-1);
}

int	parse_args(int ac, char **av, t_data *data)
{
	if (ac != 9)
	{
		fprintf(stderr, "Usage: ./codexion coders burnout compile debug \
refactor required cooldown fifo|edf\n");
		return (0);
	}
	data->count = read_positive(av[1]);
	data->burnout = read_positive(av[2]);
	data->compile_time = read_positive(av[3]);
	data->debug_time = read_positive(av[4]);
	data->refactor_time = read_positive(av[5]);
	data->required = read_positive(av[6]);
	data->cooldown = read_positive(av[7]);
	data->scheduler = read_scheduler(av[8]);
	if (data->count <= 0 || data->burnout < 0 || data->compile_time < 0
		|| data->debug_time < 0 || data->refactor_time < 0
		|| data->required <= 0 || data->cooldown < 0 || data->scheduler < 0)
	{
		fprintf(stderr, "Error: invalid arguments\n");
		return (0);
	}
	return (1);
}
