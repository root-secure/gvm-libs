/* gvm-libs/base
 * $Id$
 * Description: Implementation of API to handle globally stored preferences
 *
 * Authors:
 * Jan-Oliver Wagner <jan-oliver.wagner@greenbone.net>
 *
 * Copyright:
 * Copyright (C) 2014 Greenbone Networks GmbH
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 */

/**
 * @file prefs.c
 * @brief Implementation of API to handle globally stored preferences.
 *
 * A global store of preferences to scanner and NVTs is handled by this
 * module.
 */

#include <string.h> /* for strlen() */
#include <stdlib.h> /* for atoi() */
#include <stdio.h>  /* for printf() */
#include <glib.h>   /* for gchar */

#include "settings.h" /* for init_settings_iterator_from_file */


static GHashTable *global_prefs = NULL;

/**
 * @brief Initializes the preferences structure. If it was
 *        already initialized, remove old settings and start
 *        from scratch.
 */
static void
prefs_init (void)
{
  if (global_prefs)
    g_hash_table_destroy (global_prefs);

  global_prefs = g_hash_table_new (g_str_hash, g_str_equal);
}

/**
 * @brief Get the pointer to the global preferences structure.
 *        Eventually this function should not be used anywhere.
 */
GHashTable *
preferences_get (void)
{
  if (!global_prefs)
    prefs_init ();

  return global_prefs;
}

/**
 * @brief Get a string preference value via a key.
 *
 * @param key    The identifier for the preference.
 *
 * @return A pointer to a string with the value for the preference.
 *         NULL in case for the key no preference was found or the
 *         preference is not of type string.
 */
const gchar *
prefs_get (const gchar * key)
{
  if (!global_prefs)
    prefs_init ();

  return g_hash_table_lookup (global_prefs, key);
}

/**
 * @brief Get a boolean expression of a preference value via a key.
 *
 * @param key    The identifier for the preference.
 *
 * @return 1 if the value is considered to represent "true" and
 *         0 if the value is considered to represent "false".
 *         If the preference is of type string, value "yes" is true,
 *         anything else is false.
 *         Any other type or non-existing key is false.
 */
int
prefs_get_bool (const gchar * key)
{
  gchar *str;

  if (!global_prefs)
    prefs_init ();

  str = g_hash_table_lookup (global_prefs, key);
  if (str && !strcmp (str, "yes"))
    return 1;

  return 0;
}

/**
 * @brief Set a string preference value via a key.
 *
 * @param key    The identifier for the preference. A copy of this will
 *               be created if necessary.
 *
 * @param value  The value to set. A copy of this will be created. 
 */
void
prefs_set (const gchar * key, const gchar * value)
{
  if (!global_prefs)
    prefs_init ();

  g_hash_table_insert (global_prefs, g_strdup (key), g_strdup (value));
}

/**
 * @brief Apply the configs from given file as preferences.
 *
 * @param config    Filename of the configuration file.
 */
void
prefs_config (const char *config)
{
  settings_iterator_t settings;

  if (!global_prefs)
    prefs_init ();

  if (!init_settings_iterator_from_file (&settings, config, "Misc"))
    {
      while (settings_iterator_next (&settings))
          prefs_set (settings_iterator_name (&settings),
                     settings_iterator_value (&settings));

      cleanup_settings_iterator (&settings);
    }

  prefs_set ("config_file", config);
}

/**
 * @brief Dump the preferences to stdout
 */
void
prefs_dump (void)
{
  void *name, *value;
  GHashTableIter iter;

  g_hash_table_iter_init (&iter, global_prefs);
  while (g_hash_table_iter_next (&iter, &name, &value))
    {
      printf ("%s = %s\n", (char *) name, (char *) value);
    }
}

/**
 * @brief Returns the timeout defined by the client or 0 if none was set.
 *
 * @param oid         OID of NVT to ask timeout value of.
 *
 * @return 0 if no timeout for the NVT oid was found, timeout in seconds
 *         otherwise.
 */
int
prefs_nvt_timeout (const char *oid)
{
  char *pref_name = g_strdup_printf ("timeout.%s", oid);
  const char * val = prefs_get (pref_name);
  int timeout = (val ? atoi (val) : 0);

  g_free (pref_name);

  return timeout;
}
