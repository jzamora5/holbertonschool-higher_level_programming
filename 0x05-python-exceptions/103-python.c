#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

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

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	sizel = ((PyVarObject *)p)->ob_size;
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", sizel);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < sizel; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);

		if (PyFloat_Check(item))
			print_python_float(item);
	}

	fflush(stdout);
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

	sizeb = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

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
/**
 * print_python_float - prints some basic info about Python floats
 *
 * @p: Object of python
 *
 * Return: No Return
 */
void print_python_float(PyObject *p)
{
	double floatpy;
	char *fstr;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}


	floatpy = ((PyFloatObject *)p)->ob_fval;
	fstr = PyOS_double_to_string(floatpy, 'r', 0,
				     Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s", fstr);

	printf("\n");

}
