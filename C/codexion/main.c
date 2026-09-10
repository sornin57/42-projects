#include "codexion.h"

int	main(int ac, char **av)
{
	t_data	data;

	memset(&data, 0, sizeof(t_data));
	if (parse_args(ac, av, &data) == 0)
		return (1);
	if (init_data(&data) == 0)
	{
		free_data(&data);
		return (1);
	}
	start_simulation(&data);
	free_data(&data);
	return (0);
}
