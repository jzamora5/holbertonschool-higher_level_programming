#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
/**
 * print_python_list - prints some basic info about Python lists
 *
 * @p: Object of python
 *
 * Return: No Return
 */
void print_python_list(PyObject *p)
{
	long int i, sizel, alloc;
	PyObject *item;

	sizel = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");

	printf("[*] Size of the Python List = %ld\n", sizel);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < sizel; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 *
 * @p: Object of python
 *
 * Return: No Return
 */
void print_python_bytes(PyObject *p)
{
	long int i, sizeb;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	sizeb = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", sizeb);
	printf("  trying string: %s\n", str);

	if (sizeb < 10)
		printf("  first %ld bytes:", sizeb + 1);
	else
		printf("  first 10 bytes:"), sizeb = 9;

	for (i = 0; i <= sizeb; i++)
		if (str[i])
			printf(" %02hhx", str[i]);
		else
			printf(" 00");
	printf("\n");
}
