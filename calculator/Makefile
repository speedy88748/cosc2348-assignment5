
objective = calculator

sources = main.c addition.c subtraction.c multiplication.c division.c

objects = $(sources:.c=.o)

all: $(objective)

$(objective): $(objects)
	cc -o $(objective) $(objects)
%.o: %.c operations.h
	cc -c $< -o $@
clean:
	rm -f $(objective) $(objects)
