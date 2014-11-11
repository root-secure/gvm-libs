/* OpenVAS Libraries
 * Copyright (C) 1998 Renaud Deraison
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public
 * License along with this library; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * scanners_utils -- scanner-plugins-specific stuff
 */

#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>

#include <glib.h>

#include "network.h"
#include "internal_com.h" /* for INTERNAL_COMM_MSG_TYPE_DATA */

/**
 * @brief Sends the status of an action.
 */
int
comm_send_status (struct arglist *globals, char *hostname, char *action,
                  int curr, int max)
{
  int soc = GPOINTER_TO_SIZE (arg_get_value (globals, "global_socket"));
  char buffer[2048];

  if (soc < 0 || soc > 1024)
    return -1;

  if (strlen (hostname) > (sizeof (buffer) - 50))
    return -1;

  snprintf (buffer, sizeof (buffer),
            "SERVER <|> STATUS <|> %s <|> %s <|> %d/%d <|> SERVER\n",
            hostname, action, curr, max);

  internal_send (soc, buffer, INTERNAL_COMM_MSG_TYPE_DATA);

  return 0;
}



/*
 * 0 is considered as the biggest number, since it
 * ends our string
 */
static int
qsort_compar (const void *a, const void *b)
{
  u_short *aa = (u_short *) a;
  u_short *bb = (u_short *) b;
  if (*aa == 0)
    return (1);
  else if (*bb == 0)
    return (-1);
  else
    return (*aa - *bb);
}

/**
 * @brief Converts a string like "-100,200-1024,3000-4000,60000-" into an array
 * @brief of port numbers
 *
 * This function is (c) Fyodor <fyodor@dhp.com> and was taken from
 * his excellent and outstanding scanner Nmap
 * See http://www.insecure.org/nmap/ for details about
 * Nmap
 */
unsigned short *
getpts (char *origexpr, int *len)
{
  int exlen;
  char *p, *q;
  unsigned short *tmp, *ports;
  int i = 0, j = 0, start, end;
  char *expr;
  char *mem;
  char *s_start, *s_end;
  static unsigned short *last_ret = NULL;
  static char *last_expr = NULL;
  static int last_num;

  expr = g_strdup (origexpr);
  exlen = strlen (origexpr);
  mem = expr;

  if (last_expr != NULL)
    {
      if (strcmp (last_expr, expr) == 0)
        {
          if (len != NULL)
            *len = last_num;
          g_free (mem);
          return last_ret;
        }
      else
        {
          g_free (last_expr);
          last_expr = NULL;
          g_free (&last_ret);
          last_ret = NULL;
        }
    }




  ports = g_malloc0 (65536 * sizeof (short));
  for (; j < exlen; j++)
    if (expr[j] != ' ')
      expr[i++] = expr[j];
  expr[i] = '\0';

  if ((s_start = strstr (expr, "T:")) != NULL)
    {
      expr = &(s_start[2]);
    }

  if ((s_end = strstr (expr, "U:")) != NULL)
    {
      if (s_end[-1] == ',')
        s_end--;
      s_end[0] = '\0';
    }


  i = 0;
  while ((p = strchr (expr, ',')))
    {
      *p = '\0';
      if (*expr == '-')
        {
          start = 1;
          end = atoi (expr + 1);
        }
      else
        {
          start = end = atoi (expr);
          if ((q = strchr (expr, '-')) && *(q + 1))
            end = atoi (q + 1);
          else if (q && !*(q + 1))
            end = 65535;
        }
      if (start < 1)
        start = 1;
      if (start > end)
        {
          g_free (mem);
          g_free (ports);
          return NULL;
        }
      for (j = start; j <= end; j++)
        ports[i++] = j;
      expr = p + 1;
    }
  if (*expr == '-')
    {
      start = 1;
      end = atoi (expr + 1);
    }
  else
    {
      start = end = atoi (expr);
      if ((q = strchr (expr, '-')) && *(q + 1))
        end = atoi (q + 1);
      else if (q && !*(q + 1))
        end = 65535;
    }
  if (start < 1)
    start = 1;
  if (start > end)
    {
      g_free (mem);
      g_free (ports);
      return NULL;
    }
  for (j = start; j <= end; j++)
    ports[i++] = j;
  ports[i++] = 0;


  qsort (ports, i, sizeof (u_short), qsort_compar);
  tmp = g_realloc (ports, i * sizeof (short));
  if (len != NULL)
    *len = i - 1;
  g_free (mem);

  last_ret = tmp;
  last_expr = g_strdup (origexpr);
  last_num = i - 1;
  return tmp;
}
