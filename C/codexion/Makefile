NAME = codexion

CC = cc
CFLAGS = -Wall -Wextra -Werror -pthread
RM = rm -f

SRCS = main.c parse.c init.c time.c state.c queue.c dongle.c coder.c \
	monitor.c simulation.c
OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

%.o: %.c codexion.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
